# 🚨 Keyword Detection Application with Aho-Corasick

## 📘 목적
이 문서는 Aho-Corasick 알고리즘을 활용한 다중 키워드 기반 로그 탐지 시스템의 기본 구조와 응용 방식을 설명합니다.

---

## ⚙️ 핵심 기능

### 1. 키워드 기반 탐지
- 사용자 정의 키워드 리스트를 등록
- 로그 또는 문자열에서 해당 키워드가 포함되어 있는지 탐지

### 2. Aho-Corasick 알고리즘 사용 이유
- 다중 키워드를 동시에 탐색할 수 있음
- 시간복잡도: O(텍스트 길이)
- 정규 표현식이나 단순 반복 비교보다 월등히 빠름

### 3. 동작 구조
1. 키워드를 Trie에 등록
2. Failure Link를 구성하여 중복 비교 방지
3. 입력 로그 텍스트를 한 글자씩 읽으면서 탐색

---

## 🧪 샘플 코드 구조

```python
import ahocorasick

def analyze_event_log_aho(logs, keywords):
    A = ahocorasick.Automaton()
    for idx, keyword in enumerate(keywords):
        A.add_word(keyword.lower(), (idx, keyword))
    A.make_automaton()

    results = []
    for log in logs:
        found = set()
        for _, (_, keyword) in A.iter(log.lower()):
            found.add(keyword)
        if found:
            results.append((log, list(found)))
        else:
            results.append((log, []))
    return results
```

---

## 📤 출력 예시

```
⚠️ 탐지됨: 'SQL injection 의심 로그입니다.' | 키워드: ['sql injection']
✅ 정상: '정상 요청입니다.'
⚠️ 탐지됨: '쉘을 통해 rce를 시도하는 로그 발견' | 키워드: ['rce']
```

---

## 💡 응용 가능 분야

| 분야             | 활용 예시                                  |
|------------------|---------------------------------------------|
| 🔒 보안 탐지       | 악성 URL, 공격 패턴 자동 탐지              |
| 📄 로그 분석       | 운영 로그에서 경고 키워드 탐지              |
| 📊 모니터링 시스템 | 실시간 키워드 매칭을 통한 이상 징후 감지     |
| 📚 콘텐츠 필터링   | 불건전 단어, 욕설, 금칙어 자동 필터링       |

---

## 📌 결론
Aho-Corasick 기반 탐지 시스템은 보안성과 속도 면에서 매우 우수하며, 다중 키워드를 실시간으로 탐지해야 하는 다양한 상황에서 효과적으로 활용될 수 있습니다.
