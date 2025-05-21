def is_malicious(text, keyword_list):
    for keyword in keyword_list:
        if keyword in text.lower():
            return True
    return False

malicious_keywords = ["sql injection", "xss", "rce"]
text = "SQL Injection 공격이 있습니다."
print("탐지 결과:", is_malicious(text, malicious_keywords))
