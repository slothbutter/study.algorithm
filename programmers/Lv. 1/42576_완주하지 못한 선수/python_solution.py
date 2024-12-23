from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    decompletion = participant - completion
    return list(decompletion.keys())[0]

if __name__ == "__main__":
    participant = [["leo", "kiki", "eden"],
                   ["marina", "josipa", "nikola", "vinko", "filipa"],
                   ["mislav", "stanko", "mislav", "ana"]]
    
    completion = [["eden", "kiki"],
                  ["josipa", "filipa", "marina", "nikola"],
                  ["stanko", "ana", "mislav"]]
    
    result = ["leo", "vinko", "mislav"]
    
    for i, (participant, completion) in enumerate(zip(participant, completion)):
        if result[i] == solution(participant, completion):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(participant, completion)}이 기댓값 {result[i]}과 다릅니다.")