
# [✔️][Lv. 2] [42626. 더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626#)


문제 설명
-----

매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

```
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
```

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.  

Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

* scoville의 길이는 2 이상 1,000,000 이하입니다.
* K는 0 이상 1,000,000,000 이하입니다.
* scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
* 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

### 입출력 예

| scoville | K | return |
| --- | --- | --- |
| [1, 2, 3, 9, 10, 12] | 7 | 2 |

### 입출력 예 설명

1. 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.  
   
   새로운 음식의 스코빌 지수 = 1 + (2 \* 2) = 5  
   
   가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]
2. 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.  
   
   새로운 음식의 스코빌 지수 = 3 + (5 \* 2) = 13  
   
   가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.

---

※ 공지 - 2022년 12월 23일 테스트 케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.  

※ 공지 - 2023년 03월 23일 테스트 케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```python
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
  ```

  ### 1차 시도

  ```python
   import heapq

   def solution(scoville, K):
      heapq.heapify(scoville)
      cnt = 0
      while scoville[0] < K:
         s1 = heapq.heappop(scoville)
         s2 = heapq.heappop(scoville)
         s3 = s1 + (s2 * 2)
         heapq.heappush(scoville, s3)
         cnt += 1
      return cnt
  ```
  스코빌을 섞는 기준이 가장 낮은 스코빌 지수를 지닌 음식 + (두 번째로 낮은 스코빌 지수를 가진 음식 * 2)이므로 최소 힙을 통해 자료 구조를 만들고,
  최소 스코빌을 가진 2개를 pop해서 계산을 진행 한 후 다시 push하는 방식을 고안했다.

  ---
  <div align=center>
      <img width="964" height="788" alt="Image" src="https://github.com/user-attachments/assets/d35f153e-c402-4757-8b21-b8b10f2f00b2" />
  </div>

  모든 음식을 섞었음에도 만들 수 없는 경우를 빼먹어서 리스트가 모두 사용된 이후에도 계속 반복되기 때문에 Out of lange 에러가 발생했을 것이다.

  따라서 try except를 통해 예외 상황이 발생하면 (= 리스트가 비었음에도 반복문이 계속될 경우) -1을 반환하도록 고친다.

  ### 2차 시도

   ```python
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
  ```
  ---

  <img width="967" height="798" alt="Image" src="https://github.com/user-attachments/assets/871b2899-678e-4fd5-933e-993f67525370" />

  정답!

  ### 풀이에 대한 고찰

  오랜만에 다시 문제를 푸는데 힙에 대해 까먹어서 다시 보고 했다.  
  

  >💡 **Heap(힙)** ([참고 링크](https://valur.tistory.com/entry/programmers-JavaScript-%EB%8D%94-%EB%A7%B5%EA%B2%8C-42626))<br>
  > <br>
  > Heap(힙)은 이진트리 형태의 자료 구조임  
  > 힙에는 두 가지 종류가 있는데 각 노드 값이 자식 노드보다 크거나 같은 "최소 힙"(=내림차순),  
  > 각 노드의 값이 자식 노드보다 작거나 같은 "최대 힙"(=오름차순)이 있음  
  > 즉 리프 노드(제일 마지막 노드)의 값이 제일 작다! 그러면 "최소 힙"이고 제일 크다! 그러면 "최대 힙"임  
  > 힙은 Python의 내장 라이브러리인 heapq를 통해 사용할 수 있음(import heapq)    
  > heapq는 기본적으로 최소 힙으로 구현되어 있으며 최대 힙을 사용하기 위해서는 value를 음수로 바꾸는 꼼수가 필요함  
  >  
  >(예시)
  >```
  > import heapq
  > heap = []
  > values = [1,5,3,2,4]
  > # 아래 for문을 실행시키고 나면 heap은 [-5,-4,-3,-1,-2]가 된다.
  > for value in values:
  >    heapq.heappush(heap, -value)
  > # 아래 for문을 실행시키면 5,4,3,2,1이 출력된다. 즉, 큰 숫자부터 출력이 된다.
  > for i in range(5):
  >    print(-heapq.heappop(heap))
  >```
  > heapq에는 주요 3가지 기능이 있음  
  > heapq.heappop(heap)은 우리가 흔히 말하는 pop 기능과 동일하게 값을 뽑아 옴  
  > heapq.heappush(heap, value)는 우리가 흔히 말하는 push 기능과 동일하게 값을 집어 넣음   
  >단, 여기서 위의 두 기능은 힙의 불변성을 해치지 않게 집어넣음 즉, 리프 노드에 바로 집어 넣은는게 아니라 최소 힙(또는 최대 힙)을 유지하며 값을 집어넣음 따라서 자동 정렬되는 효과가 존재함  
  > heapq.heapify(list)는 리스트를 최소 힙으로 바꿔줌 만약, 최대 힙으로 사용하고 싶다면 위와 비슷하게 부호 반전의 꼼수를 사용해야함

  ## 회고
  오랜만에 다시풀어서 heap에 사용법에 대해서는 조금 검색해보고 풀었지만, 풀이 방식이 바로 떠올랐던 것을 보면 그래도 예전에 쌩으로 풀었을 때 보단 좀 더 알고리즘에 익숙해진 느낌이었다. 
</details>
<br>
<span style="color:gray"> #힙(Heap) </span>
