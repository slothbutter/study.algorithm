import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        try:
            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
            s3 = s1 + (s2 * 2)
            heapq.heappush(scoville, s3)
            cnt += 1
        except:
            return -1
    return cnt
    
if __name__ == "__main__":
    test =[
        [1, 2, 3, 9, 10, 12],
        [1, 1, 1]
    ]
    K = [7, 8]
    result = [2, -1]
    
    for i, (t, k) in enumerate(zip(test, K)):
        if result[i] == solution(t[:], k): # 리스트를 복사하여 원본을 보존
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(t, k)}이 기댓값 {result[i]}과 다릅니다.")
        