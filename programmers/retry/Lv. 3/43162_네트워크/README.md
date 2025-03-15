
# ❌[Lv. 3] [43162. 네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)


문제 설명
-----

네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

### 제한사항

* 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
* 각 컴퓨터는 0부터 `n-1`인 정수로 표현합니다.
* i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
* computer[i][i]는 항상 1입니다.

### 입출력 예

| n | computers | return |
| --- | --- | --- |
| 3 | [[1, 1, 0], [1, 1, 0], [0, 0, 1]] | 2 |
| 3 | [[1, 1, 0], [1, 1, 1], [0, 1, 1]] | 1 |

### 입출력 예 설명

예제 #1  

아래와 같이 2개의 네트워크가 있습니다.  

![image0.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/5b61d6ca97/cc1e7816-b6d7-4649-98e0-e95ea2007fd7.png)

예제 #2  

아래와 같이 1개의 네트워크가 있습니다.  

![image1.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/7554746da2/edb61632-59f4-4799-9154-de9ca98c9e55.png)



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```
  (30분 만에 풀이 실패 -> 답 보고 추후에 다시 풀어보자..)
  ```

  ### 1차 시도

  ```python
  # DFS

  def DFS(n, computers, connect, computer): # (connect, computer) == (x, y)
      if not (0 <= connect < n and 0 <= computer < n and computers[computer][connect] != 0):
          return False
      
      computers[computer][connect] = 0 # 방문처리
      
      DFS(n, computers, connect + 1, computer) # 상
      DFS(n, computers, connect - 1, computer) # 하
      DFS(n, computers, connect, computer + 1) # 좌
      DFS(n, computers, connect, computer - 1) # 우
      
      return True

  def solution(n, computers):
      answer = 0
      for computer in range(n):
          for connect in range(n):
              if DFS(n, computers, connect, computer):
                  answer += 1
      return answer
  ```

  예시에 보면 정답이 1의 군집의 개수로 나타난다. 따라서 "음료수 얼려먹기"문제와 동일하게 풀이했다.<br>

  ---

  <div align=center>
    <img src=https://github.com/user-attachments/assets/22166f8a-c931-461a-bad5-6523fb300f90 />
  </div>

  ### 풀이에 대한 고찰

  위 이미지를 보면 특수한 두 Case 말고는 모두 틀렸다.<br>
  반례를 잘 생각해보니 1의 군집은 2개이지만 네트워크 개수는 1개인 경우가 존재했다. <br>
  ex) n = 4라고 하고 2 - 1 - 3 - 4로 네트워크가 연결되었다고 했을 때 <br>
  computers는 아래와 같다.
  ```python
    computers = [
      [1, 1, 1, 0],
      [1, 1, 0, 0],
      [1, 0, 1, 1],
      [0, 0, 1, 1]
    ]
  ```
  따라서 1의 군집은 2개이지만 네트워크 자체는 1개인 반례가 생성된다.

  >💡 **제목** (참고 링크)<br>
  > <br>
  > (내용)


  ### 코드
  ```
  (내용)
  ```
  ### 설명
  (내용)

  ### 출처
  (내용)

  ## 회고
  (내용)
</details>
<br>
<span style="color:gray"> #깊이/너비 우선 탐색(DFS/BFS) </span>
