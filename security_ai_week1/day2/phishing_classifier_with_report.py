# 피싱 URL 분류 및 리포트 자동 저장 전체 코드
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# CSV 파일에서 피싱 URL 데이터 불러오기
df = pd.read_csv("data/phishing_url_sample.csv")  # 'url'과 'label' 열 포함

# TF-IDF 벡터 변환기 생성
vectorizer = TfidfVectorizer()  # URL을 벡터로 변환 (단어별 희귀성 반영)

# URL 텍스트 데이터를 TF-IDF 벡터로 변환
X = vectorizer.fit_transform(df["url"])  # 입력 특징 벡터 (X)

# 레이블(정답값) 추출: 1은 피싱, 0은 정상
y = df["label"]  # 출력 레이블 벡터 (y)

# 학습용 데이터와 테스트용 데이터로 분할 (80% 학습, 20% 테스트)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 나이브 베이즈 분류기 모델 생성
model = MultinomialNB()  # Multinomial: 이산형 특징(TF-IDF, BoW)에 적합

# 학습 데이터를 기반으로 모델 학습
model.fit(X_train, y_train)

# 테스트 데이터로 예측 수행
y_pred = model.predict(X_test)

# 예측 결과 평가 출력
print("📊 분류 리포트 (정밀도, 재현율, F1 점수):")
print(classification_report(y_test, y_pred, target_names=["정상", "피싱"]))

# Confusion Matrix 시각화
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("예측")
plt.ylabel("실제")
plt.show()

# 예측 결과 포함된 리포트를 저장
report_df = df.iloc[y_test.index].copy()
report_df["예측"] = y_pred
report_df.to_csv("phishing_detection_report.csv", index=False)
