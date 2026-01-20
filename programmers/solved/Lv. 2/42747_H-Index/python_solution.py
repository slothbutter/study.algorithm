# 자기를 포함해서 앞에 있는 것 개수만 세서 하면 되는거 아닌가?
def solution(citations):
    citations = sorted(citations, reverse=True)
    h_index = -1
    # h = 인용 수, i+1 = 자신(포함)보다 인용 수가 많은 논문의 수
    for i, h in enumerate(citations):
        h_index = max(h_index, min(i+1, h))
    return h_index
    
if __name__ == "__main__":
    citations = [[3, 0, 6, 1, 5], [10, 8, 5, 4, 3], [25, 8, 5, 3, 3]]
    result = [3, 4, 3]
    
    for i, s in enumerate(citations):
        if result[i] == solution(s):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(s)}이 기댓값 {result[i]}과 다릅니다.")
        