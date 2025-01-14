def solution(s):
    return "{0} {1}".format(min(map(int, s.split())), max(map(int, s.split())))

if __name__ == "__main__":
    n_list =["1 2 3 4", "-1 -2 -3 -4", "-1 -1"]
    result = ["1 4", "-4 -1", "-1 -1"]
    
    for i, n in enumerate(n_list):
        if result[i] == solution(n):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(n)}이 기댓값 {result[i]}과 다릅니다.")