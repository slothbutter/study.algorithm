# today : 오늘 날짜
# terms : 약관 유효기간 (종류 달)
# privacies : 약관 정보 (수집날짜 약관종류)

def convert_day(day : str) -> int:
    today_year, today_month, today_day = map(int, day.split("."))
    return (today_year * 12 * 28) + (today_month * 28) + today_day

def solution(today, terms, privacies):
    current = convert_day(today)
    privacy_kind = {t.split(" ")[0] : int(t.split(" ")[1]) * 28 for t in terms}
    
    answer = []
    for i, p in enumerate(privacies, start=1):
        day, p_kind = p.split(" ")
        if convert_day(day) + privacy_kind[p_kind] <= current:
            answer.append(i)
    
    return answer
    
    
if __name__ == "__main__":
    today = ["2022.05.19", "2020.01.01"]
    terms = [
        ['A 6', 'B 12', 'C 3'],
        ['Z 3', 'D 5']
        ]
    privacies = [
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
        ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    ]
    test_case = list(zip(today, terms, privacies))
    result = [[1, 3], [1, 4, 5]]
    
    for i, (today, terms, privacies) in enumerate(test_case):
        if result[i] == solution(today, terms, privacies):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(today, terms, privacies)}이 기댓값 {result[i]}과 다릅니다.")