def analyze_event_log(logs, keywords):
    for log in logs:
        found = []
        for keyword in keywords:
            if keyword in log.lower():
                found.append(keyword)
        if found:
            print(f"⚠️ 탐지됨: '{log}' | 키워드: {found}")
        else:
            print(f"✅ 정상: '{log}'")
