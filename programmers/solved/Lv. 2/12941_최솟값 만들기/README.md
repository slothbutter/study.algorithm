
# ✔️[Lv. 2] [12941. 최솟값 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12941)


문제 설명
-----

길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.   

배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

예를 들어 A = `[1, 4, 2]` , B = `[5, 4, 4]` 라면

* A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
* A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
* A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)

즉, 이 경우가 최소가 되므로 **29**를 return 합니다.

배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

### 제한사항

* 배열 A, B의 크기 : 1,000 이하의 자연수
* 배열 A, B의 원소의 크기 : 1,000 이하의 자연수

### 입출력 예

| A | B | answer |
| --- | --- | --- |
| [1, 4, 2] | [5, 4, 4] | 29 |
| [1,2] | [3,4] | 10 |

### 입출력 예 설명

입출력 예 #1  

문제의 예시와 같습니다.

입출력 예 #2  

A에서 첫번째 숫자인 1, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 4) 다음, A에서 두번째 숫자인 2, B에서 첫번째 숫자인 3을 뽑아 곱하여 더합니다. (누적된 값 : 4 + 6 = 10)  

이 경우가 최소이므로 10을 return 합니다.



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```
  (작성한 정답 코드를 게시 -> 실패하면 작성x)
  ```

  ### 1차 시도

  ```python
  from functools import reduce
  from math import prod
  def solution(A,B):
      return reduce(lambda x, y: prod(x) + y, zip(sorted(A), sorted(B, reverse=True)))
  ```

  문제에서 두 리스트의 누적 곱이 최소가 되게 해야하므로 큰 수와 작은 수를 서로 곱하면 된다.<br>

  1. A와 B를 한 쪽은 오름차순으로 다른 쪽은 내림차순으로 정렬한다.
  2. reduce를 통해 계산할 것이므로 하나의 iterator로 만들기 위해 zip을 사용하여 같은 index끼리 묶는다.(그럼 큰 수와 작은 수가 서로 묶인다.)
  3. reduce를 사용하여 누적 합을 구한다. 그 과정에서 묶인 데이터의 곱을 구한다.

  ---

  <div align=center>
    <img width="636" alt="Untitle" src="https://github.com/user-attachments/assets/2f14209a-b2fc-4a75-ae8e-818db08716ca" />
  </div>

  type 에러가 발생했다. 아마 zip으로 인해서 묶인 tuple 때문인 것 같은데 뭐가 문제인지....
  
  ### 풀이에 대한 고찰

  우리들의 친구 GPT를 통해 에러를 분석해보았다.(GPT 없을 때는.. 뭐가 문제였는지 하루종일 찾아다녔는데.. 역시 GPT가 예상 결과를 도출해주니 분석할 때 편한 것 같다.)<br>
  <br>
  reduce를 사용할 때는 ```x```쪽이 무조건 누적 결과로 이용되는 듯 하다. 따라서 위 코드의 문제점은 ```y```부분에 튜플이 들어가게 되고 튜플과 정수형을 연산하려고 하니 TypeError가 발생하는 것이다.<br>

  ### 2차 시도
  
  ```python
  from functools import reduce
  from math import prod
  def solution(A,B):
      return reduce(lambda x, y: x + prod(y), zip(sorted(A), sorted(B, reverse=True)), 0)
  ```

  ---

  <div align=center>
    <img width="966" alt="Untitle" src="https://github.com/user-attachments/assets/063e6216-a0a9-481d-9359-39c47de65368" />
  </div>

  ### 풀이에 대한 고찰

  문제가 발생한 부분은 이전에 연산했던 부분인 ```x```를 prod로 재연산하고 y 부분은 튜플로 놓아두어서 발생한 문제이므로 누적되는 부분(이전에 연산했던 값이 들어가는 부분)인 ```x```는 그대로 놓아두고 튜플이 들어오는 ```y```부분을 prod를 통해 곱한다.<br>
  여기서 x는 첫 연산에서 첫 번째 원소(튜플)가 들어오는 자리이기도 하므로 초기 값을 첫 번째 원소가 아닌 0으로 두어 TypeError를 방지한다.<br>

  ## 다른사람 풀이

  ### 코드1
  ```python
  # 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
  # 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
  def getMinSum(A, B):
      return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])


  # 아래 코드는 출력을 위한 테스트 코드입니다.
  print(getMinSum([1, 2], [3, 4]))
  ```
  ### 설명
  개편 전의 코드라서 위와 포맷이 약간 다르다.<br>
  ```python
  def solution(A, B):
      return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
  ```
  위 코드는 현재의 포맷으로 코드를 고친 것이다. 시험해보고 싶다면 위의 코드를 사용하면 된다.<br>
  <br>
  이 코드가 나의 코드와 크게 논리적인 로직이 다른 것은 아니다. 다만, 풀이에 사용한 함수가 달라서 기록한다.<br>
  <br>
  로직은 다르지 않지만 이 코드는 두 리스트의 곱으로 이뤄진 하나의 리스트를 만들고 sum을 통해 모든 리스트의 누적 합을 사용한다. 코드의 가독성은 개인적으로 내 코드보다 더 낫다고 평가하고 싶다.

  ### 코드2

  ```python
  # 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
  # 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
  def getMinSum(A,B):
      return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))

  #아래 코드는 출력을 위한 테스트 코드입니다.

  print(getMinSum([1,2],[3,4]))
  ```
  ### 설명
  개편 전의 코드라서 위와 포맷이 약간 다르다.<br>
  ```python
  def solution(A,B):
      return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))
  ```
  위 코드는 현재의 포맷으로 코드를 고친 것이다. 시험해보고 싶다면 위의 코드를 사용하면 된다.<br>
  이 코드를 기록한 이유도 위와 동일하다.<br>
  <br>
  로직은 다르지 않지만 map을 통해 두 리스트를 입력으로 받아 lambda 함수에 넣어 iterator를 만든다. 이후 sum을 통해 iterator의 모든 요소의 합을 구한다.
  <br>
  코드의 가독성은 이 코드가 가장 좋다고 평가하고 싶다.

  ### 출처
  [프로그래머스 다른사람 풀이](https://school.programmers.co.kr/learn/courses/30/lessons/12941/solution_groups?language=python3)

  ## 회고
  로직 자체는 그렇게 어려운 부분은 아니었다. 단지 다른 사람들의 코드와 비교해서 한 줄 코딩에 너무 치중한 결과 쉬운 함수들을 놔두고 내장 함수이지만 다른 내장 라이브러리에 있는 함수를 사용했고 좀 더 어려운 사용법을 지닌 함수들을 사용해서 아쉬운 점이 있다.<br>
  <br>
  다양한 솔루션이 있다면 그 중 가장 단순한 솔루션이 가장 좋은 솔루션이라는 ```오캄의 면도날 법칙```을 기억하자..

</details>
<br>
<span style="color:gray"> #정렬 </span>
