def solution(s):
    result = [0, 0]
    while s != "1":
        for c in s:
            if c == "0":
                result[1] += 1
            else:
                pass
        s = s.replace("0", "")
        s = format(len(s), "b")
        result[0] += 1
    return result
    
if __name__ == "__main__":
    s_list = ["110010101001", "01110", "1111111"]
    result = [[3, 8], [3, 3], [4, 1]]
    
    for i, s in enumerate(s_list):
        if result[i] == solution(s):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(s)}이 기댓값 {result[i]}과 다릅니다.")
        