# 📦 Additional Study: Security Extension of Text Preprocessing

## 📌 확장 주제: 텍스트 전처리 → 보안 응용

### 🔍 학습 범위 확장
- 텍스트 정규화
- 토큰화 (`word_tokenize`, `WordPunctTokenizer`, `TreebankWordTokenizer`)
- 벡터화 (`CountVectorizer`, `TfidfVectorizer`)
- TF vs TF-IDF의 차이 이해

---

## 🔐 보안 적용 가능성

### 1. 악성 URL / 문서 탐지
- 특수문자 제거 및 토큰화 → TF-IDF → 분류
- 예시: 피싱 URL 탐지

### 2. 로그 기반 이상 행위 탐지
- 로그 메시지 전처리 후 벡터화 → 이상 탐지 모델
- 예시: 내부 사용자 이상행위 탐지

### 3. 보안 인텔리전스 자동화
- 블로그/다크웹 크롤링 후 키워드 추출
- 예시: 공격 그룹별 위협 키워드 수집

### 4. 소셜 엔지니어링 분석
- 이메일/DM 분석 → 감정/의도 분석
- 예시: 피싱 감정유도 탐지

---

## 💡 실습 아이디어

| 프로젝트 이름 | 설명 | 사용 기술 |
|---------------|------|-----------|
| 피싱 URL 탐지기 | TF-IDF + Naive Bayes 분류기 | TfidfVectorizer, sklearn |
| 로그 이상 탐지 | 로그 전처리 후 이상치 탐지 | CountVectorizer, IsolationForest |
| 다크웹 키워드 수집기 | 크롤링 + 키워드 벡터화 | BeautifulSoup, TF-IDF |

---

## 🧠 다음 학습 제안
- TF-IDF + Naive Bayes 실습
- LSTM 기반 시퀀스 이상 탐지
- NER 기반 IOC 추출

