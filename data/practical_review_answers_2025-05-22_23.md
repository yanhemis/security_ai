# 📘 Practical Review Answers - 2025-05-22 ~ 2025-05-23

## 🧠 개념 복습 문제 정답
(생략: 이전 응답 참고)

---

## 🧪 실습 응용 문제 정답 예시

### 1. 모델 평가 지표 출력 코드 (주석 포함)
```python
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 테스트 데이터를 예측
y_pred = model.predict(X_test)

# 정밀도, 재현율, F1 점수 등의 지표 출력
print(classification_report(y_test, y_pred))

# Confusion Matrix 생성
cm = confusion_matrix(y_test, y_pred)

# Heatmap으로 시각화
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.show()
```

---

### 2. Suffix Array 및 LCP 배열 구현 코드 (주석 포함)
```python
def build_suffix_array(s):
    # 모든 접미사를 정렬하여 인덱스를 반환
    return sorted(range(len(s)), key=lambda i: s[i:])

def build_lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    for i, suffix in enumerate(sa):
        rank[suffix] = i  # Suffix Array에서 각 인덱스의 순위 저장

    lcp = [0] * (n - 1)  # LCP 배열 초기화
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]  # 다음 접미사
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1  # 공통 접두사 길이 증가
        lcp[rank[i]] = k  # LCP 저장
        if k: k -= 1  # 다음 비교를 위해 감소
    return lcp

s = "banana"
sa = build_suffix_array(s)
lcp = build_lcp_array(s, sa)
print("Suffix Array:", sa)
print("LCP Array:", lcp)
```

---

### 3. Aho-Corasick 키워드 탐지 예시 코드 (주석 포함)
```python
import ahocorasick

# Aho-Corasick 자동화 객체 생성
A = ahocorasick.Automaton()

# 탐지할 키워드 추가
keywords = ["sql", "xss", "injection", "admin"]
for idx, key in enumerate(keywords):
    A.add_word(key, (idx, key))

# 실패 링크 등 내부 구조 자동 생성
A.make_automaton()

# 테스트할 텍스트
text = "user=admin&input=DROP TABLE users;"

# 매칭되는 키워드 출력
for end_index, (idx, word) in A.iter(text):
    start_index = end_index - len(word) + 1
    print(f"⚠️ 키워드 '{word}' 발견: 위치 {start_index}-{end_index}")
```
