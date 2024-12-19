# ✔️[[Silver IV] 1920. 수 찾기](https://www.acmicpc.net/problem/1920)

## 문제 설명

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

### 입력

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

### 출력

 M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

### 예제 입력1

```
5
4 1 5 2 3
5
1 3 7 9 5
```

### 예제 출력1

```
1
1
0
0
1
```
<details>
  <summary><h2>내 풀이(Python)</h2></summary>

### 정답 코드

```python
import sys

def binary_search(a,x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


input_n = int(sys.stdin.readline())
integer_n = list(sys.stdin.readline().split())

input_m = int(sys.stdin.readline())
integer_m = list(sys.stdin.readline().split())
## integer_m2 = []

integer_n.sort()
## integer_n.sort(key = lambda x : x[0])

## 중복 제거
'''
for value in integer_m:
    if value not in integer_m2:
        integer_m2.append(value)
'''

for i in range(input_m) :
     print(binary_search(integer_n, integer_m[i]))
```

### 1차 시도

```python
def binary_search(a,x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

integer_n = []
integer_m = []

input_n = int(input())
integer_n = input().split()

input_m = int(input())
integer_m = input().split()

integer_n.sort(key = lambda x : x[0])

for i in range(input_n):
    print(binary_search(integer_n, integer_m[i]))
```

1. 먼저 저장할 리스트를 만든다.
2. 문제에 맞게 입력을 받는다.
3. 이진 탐색을 사용해야하므로 비교 해야하는 리스트를 정렬해준다.
4. 이진 탐색을 통해 리스트 안에 원소들이 있는지 확인한다.

----

개같이 멸망…

![Untitled](https://github.com/user-attachments/assets/f52eaa41-9514-4921-9119-46d19253e352)

10% 까지 검사하다가 바로 틀렸다고 나오는 걸로 봐서는 첫 번째 또는 두 번째 테스트 케이스에서 틀린 것 같다.

알고리즘은 문제가 없어 보여서 반례를 검색해서 모두 돌려보았는데 모두 문제없이 출력되었다.

### 2차 시도

```python
def binary_search(a,x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


input_n = int(input())
integer_n = list(input().split())

input_m = int(input())
integer_m = list(input().split())
integer_m2 = []

integer_n.sort(key = lambda x : x[0])

## 중복 제거
for value in integer_m:
    if value not in integer_m2:
        integer_m2.append(value)


for i in range(len(integer_m2)) :
    print(binary_search(integer_n, integer_m2[i]))
```

혹시 m 입력에서 중복된 값이 입력되면 (예시 : 1 1) 중복된 값 모두를 체크하기 때문에 틀렸는지 확인을 위해 중복을 제거하는 코드를 삽입해 주었다.

----

이번엔 시간 초과가 된다. 아마 중복 제거가 추가로 들어가서 그런 것 같다.

## 풀이에 대한 고찰

일단 저 항목인 sort()에 대해 알아보도록 하자.

파이썬에서 정렬을 수행하는 기본 메소드는 sort(), sorted()가 있다. 얘내들은 같은 기능을 수행하지만 동작방식에는 큰 차이점이 있다.

쉽게 설명하면 sort()는 그냥 원래 리스트에서 정렬을 한 것이고, sorted()는 원래 리스트를 정렬한 다른 리스트를 생성한다.

여기서 sort()와 sorted() 모두 정렬 기준이라고 할 수 있는 key 값이 필요한데 이 키 값은 비워두면 기본적으로 오름차순 정렬을 수행한다.

또한 리스트의 원소가 튜플인 경우 정렬 기준을 튜플 항목으로 지정할 수 있는데 이런게 바로 “key = lambda x : x[0]” 이 부분이다.

이 코드는 list x 의 튜플 중 [0]번째 튜플을 기준으로 오름차순 정렬하겠다는 의미이다. ( 참고로 “key = lambda x : -x[0]”이면 내림차순 정렬이다.)

따라서  “integer_n.sort(key = lambda x : x[0])” 이 코드는 “integer_n을 0번째 튜플 항목을 기준으로 오름차순으로 정렬하겠다” 는 의미이다. 

여기서 리스트 integer_n의 원소들을 보면 튜플이 아닌 그냥 원소들로 저장이 되어있으므로 이러한 오류가 생긴 것 같다.

사실 실행에 있어서는 아무 문제가 없지만 이는 단순히 파이썬의 내장 인터프리터가 묵시적으로 바꿔준 것이라고 생각한다.

따라서 실행에 있어서는 문제가 없지만, 정답은 아닌 아이러니한 상황이 발생한 것 같다.

## 다른 사람 풀이
### 코드
```python
from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')
```

### 설명
1. 입력받을 개수인 n을 입력받는다.
2. set 타입 ( 집합 타입 )으로 n 개수 만큼 입력받는다.
3. 같은 방법으로 m, M을 입력받는다.
4. for 문을 이용해 M의 각 항을 l에 대입하여 반복한다. (예시 : M = [ 1, 2, 3 ] 이면 l에 순서대로 대입 후 for문 수행)
5. 대입된 l과 N을 조건에 맞게 비교한다. (여기서는 조건부 표현식으로 사용)

> [!NOTE]
> **파이썬에서 조건문**(https://wikidocs.net/20)<br>
> <br>
>파이썬에서는 조건문을 다양하게 표현 할 수 있다.
>위 코드에서 “stdout.write('1\n') if l in N else stdout.write('0\n')” 이렇게 >조건문을 표현 한 것을 조건부 표현식이라 한다.
>조건부 표현식의 형태는 ”조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우”이다.
>이러한 조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어서 좋다.

### 출처
https://chancoding.tistory.com/44

## 회고
![Untitled2](https://github.com/user-attachments/assets/ff8c7fe7-58d9-4a3e-8488-1005b8f55ad9)

수많은… 뻘짓의 노력들…

### 참고 자료
(참고 링크)
</details>
<br>
<span style="color:gray"> #자료 구조 #정렬 #이분 탐색 #해시를 사용한 집합과 맵 </span>
