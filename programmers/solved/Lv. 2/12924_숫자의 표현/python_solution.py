from collections import deque
def solution(n):
    n_que = deque(range(1, n+1))
    select_que = deque()
    cnt = 0
    
    while n_que:
        if sum(select_que) > n:
            select_que.popleft()
        elif sum(select_que) < n:
            select_que.append(n_que.popleft())
        elif sum(select_que) == n:
            select_que.append(n_que.popleft())
            cnt += 1
    return cnt + 1        
    
if __name__ == "__main__":
    n_list =[15, 3, 6, 10]
    result = [4, 2, 2, 2]
    
    for i, n in enumerate(n_list):
        if result[i] == solution(n):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(n)}이 기댓값 {result[i]}과 다릅니다.")
        