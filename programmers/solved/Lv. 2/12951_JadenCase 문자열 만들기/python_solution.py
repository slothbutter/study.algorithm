def solution(s):
    words = []
    for w in s.split(" "):
        if w == "":
            words.append("")
        elif not w[0].isdigit():
            words.append(w[0].upper() + w[1:].lower())
        else:
            words.append(w[0] + w[1:].lower())
    return ' '.join(words)
    
if __name__ == "__main__":
    # 공백에 관련된 반례로 "  for the what  1what  "가 있음
    s_list =["3people unFollowed me", 
             "for the last week", 
             "  for the what  1what  "] 
    result = ["3people Unfollowed Me",
              "For The Last Week",
              "  For The What  1what  "]
    
    for i, s in enumerate(s_list):
        if result[i] == solution(s):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(s)}이 기댓값 {result[i]}과 다릅니다.")
        