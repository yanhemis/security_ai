# ✅ Practical Review Task - 2025-05-22 ~ 2025-05-23

## 🧠 개념 복습 문제

1. **나이브 베이즈 분류기에서 ‘사전 확률’과 ‘가능도’는 무엇을 의미하며, 각각은 어떤 방식으로 모델 학습에 기여하는가?**

2. **TF-IDF의 ‘IDF’는 어떤 목적을 갖고 있으며, CountVectorizer와 비교했을 때 장점은 무엇인가?**

3. **BernoulliNB, MultinomialNB, GaussianNB 각각의 사용 조건과 가장 적절한 데이터 타입을 설명하시오.**

4. **Confusion Matrix에서 `precision`, `recall`, `f1-score`는 무엇을 의미하며 각각 어떤 상황에서 중요한가?**

5. **Aho-Corasick 알고리즘의 작동 방식에서 Trie와 실패 링크의 역할은 무엇인가?**

6. **Suffix Array는 어떤 자료구조이며, 문자열 검색 시 어떤 방식으로 효율성을 높이는가?**

7. **LCP(Longest Common Prefix) 배열은 왜 필요한가? 어떤 상황에서 검색 효율을 높여주는가?**

---

## 🧪 실습 응용 문제

1. **`MultinomialNB` 모델 학습 후, 아래 지표들을 출력하는 코드를 직접 작성하시오:**
   - 정확도 (accuracy)
   - 정밀도 (precision)
   - 재현율 (recall)
   - F1-score
   - confusion matrix heatmap 시각화 포함

2. **Suffix Array와 LCP 배열을 직접 Python 코드로 구현해보고, “banana” 문자열을 기준으로 출력 결과를 확인하시오.**

3. **Aho-Corasick 알고리즘을 구현하거나 제공된 구현을 활용하여 다중 키워드 탐지 실험을 진행하시오.**
   - 입력 키워드 예시: `["sql", "xss", "injection", "admin"]`
   - 테스트 텍스트 예시: `"user=admin&input=DROP TABLE users;"`

---

## 🧩 통합 심화 과제

**실시간 보안 탐지기 구성하기 (선택형 과제)**  
TF-IDF 기반 분류기와 Aho-Corasick 알고리즘을 조합하여 간단한 실시간 보안 탐지기를 설계하고, 아래 기능을 구현하세요:
- 의심 URL 텍스트 입력 시 다중 키워드 탐지
- 입력된 텍스트의 분류 결과 (정상/위험) 출력
- 탐지 결과를 `.csv`로 저장
