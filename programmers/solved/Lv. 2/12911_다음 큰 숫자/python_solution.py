def solution(n):
    next_num = n + 1
    while format(n, "b").count("1") != format(next_num, "b").count("1"):
        next_num += 1
    return next_num    
    
if __name__ == "__main__":
    n_list =[78, 15]
    result = [83, 23]
    
    for i, n in enumerate(n_list):
        if result[i] == solution(n):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(n)}이 기댓값 {result[i]}과 다릅니다.")
        