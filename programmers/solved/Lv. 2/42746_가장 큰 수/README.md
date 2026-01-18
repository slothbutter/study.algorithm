
# ✔️[Lv. 2] [42746. 가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)


문제 설명
-----

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

* numbers의 길이는 1 이상 100,000 이하입니다.
* numbers의 원소는 0 이상 1,000 이하입니다.
* 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

### 입출력 예

| numbers | return |
| --- | --- |
| [6, 10, 2] | "6210" |
| [3, 30, 34, 5, 9] | "9534330" |

---

※ 공지 - 2021년 10월 20일 테스트케이스가 추가되었습니다.



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```python
  from functools import cmp_to_key
  def solution(numbers):
      def sort_condition(a, b):
          if a+b > b+a:
              return -1
          elif a+b < b+a:
              return 1
          else:
              return 0
      numbers = list(map(str, numbers))
      sorted_numbers = sorted(numbers, key=cmp_to_key(sort_condition))
      result = ''.join(sorted_numbers)
      if int(result) == 0:
          return '0'
      else:
          return result
  ```

  ### 1차 시도

  ```python
  def solution(numbers):
    numbers = list(map(str, numbers))
    sorted_numbers = sorted(numbers, key=lambda x: (-len(x), x), reverse=True)
    return ''.join(sorted_numbers)
  ```
  
  단순 정렬로 풀어보려고 했지만 수의 길이가 더 길지만 앞에 와야하는 케이스를 처리하지 못해서 실패했다.
  다양한 케이스로 시도를 해봤을 때 단순한 정렬기준 보다는 다른 정렬기준이 필요할 것 같다.

  ---

  <img width="949" height="214" alt="image" src="https://github.com/user-attachments/assets/8c1f340a-4194-412f-bfb1-d86f99a2e481" />  
  
  <img width="943" height="100" alt="image" src="https://github.com/user-attachments/assets/4d03d540-79e2-4f50-89ba-4ba15f96ae89" />

  ### 2차 시도(힌트 사용)

  ```python
  def sort_condition(a, b):
        if a+b > b+a:
            return -1
        elif a+b < b+a:
            return 1
        else:
            return 0
    numbers = list(map(str, numbers))
    sorted_numbers = sorted(numbers, key=cmp_to_key(sort_condition))
    result = ''.join(sorted_numbers)
    if int(result) == 0:
        return '0'
    else:
        return result
  ```
  >💡 **비교 함수(Comparator)로 정렬하라** (GPT 힌트)<br>
  > <br>
  > 각 숫자를 문자열로 바꿔서 정렬할 때:  
  > &ensp; a가 b보다 앞에 와야 하는 조건: a+b > b+a  
  > &ensp; (문자열 비교로도 OK — 같은 길이로 비교되기 때문)

  GPT힌트에서 영감을 받아서 문제를 풀었다.  
  먼저 각 숫자 문자열을 앞+뒤 와 뒤+앞을 비교한 후 더 큰 순서대로 정렬한다.  
  간단하지만 functools.cmp_to_key 함수를 활용해야 풀 수 있는 방식이다.  

  >💡 **functools.cmp_to_key** (https://wikidocs.net/109303)<br>
  > <br>
  > cmp_to_key는 두 원소의 상대적인 정렬 순서를 직접 정의하고 싶을 때 사용하는 함수다.  
  > 비교 함수 cmp(a, b)는 항상 다음 규칙을 따른다.  
  >  •	음수 반환: a가 b보다 앞에 와야 한다  
  >  •	0 반환: a와 b의 순서는 동일하다  
  >  •	양수 반환: a가 b보다 뒤에 와야 한다  
  > <br>
  > 여기서 중요한 점은, a와 b는  
  > 정렬 알고리즘이 임의로 선택한 두 원소이며  
  > 리스트에서의 현재 위치나 인덱스와는 무관하다는 것이다.
  > <br>  
  > 예를 들어 numbers가 ["1", "2", "3", "4"]일 때,  
  > 정렬 중 "1"과 "2"가 비교되면:  
  >   •	"1" + "2" = "12"  
  >   •	"2" + "1" = "21"  
  > "21"이 더 크므로 "2"가 "1"보다 앞에 와야 한다.  
  > 따라서 cmp("1", "2")는 양수를 반환하고,  
  > 이는 "1"을 "2"보다 뒤에 배치하라는 의미가 된다.  
  > <br> 
  > 이와 같은 비교를 모든 원소 쌍에 대해 반복하여  
  > 최종적으로 가장 큰 수를 만들 수 있는 순서가 결정된다.

  

  

  ---

  <img width="942" height="305" alt="image" src="https://github.com/user-attachments/assets/43b6d61b-5dc3-4f29-a4e6-6cc91182bb4d" />

  ### 다른 사람 풀이


  ### 코드
  ```python
  def solution(numbers):
      numbers = list(map(str, numbers))
      numbers.sort(key=lambda x: x*3, reverse=True)
      return str(int(''.join(numbers)))
  ```
  ### 설명
  
  문자열 길이를 3배 하여 비교하는 방식이다.  
  예를 들면 [3, 34, 334]이 존재할 때, 정렬되는 순서는 [334, 34, 3]일 것이다.
  이러한 정렬을 구현하기 위해 3과 34를 최대 자릿수까지 늘려주는 작업이 필요하다.
  따라서 원본 배열을 3배(100의 자리수 까지 늘림)하면 [333, 343434, 334334334]가 되고
  이 수를 정렬하면 [334, 34, 3]이 되는 구조이다.

  우리가 풀지 못했던 케이스에서 살펴보자.
  [3, 30, 34, 5, 9]의 경우 올바른 정렬 순서는 [9, 5, 34, 3, 30]이다.
  위 로직에 따라 key는 [333, 303030, 343434, 555, 999]가 된다.
  자료형이 int가 아니라 string 이므로 먼저 제일 첫 자리를 비교하게 된다.
  999, 555가 제일 앞에 오게되고 [333, 303030, 343434]를 비교하기 위해 그 다음 자리를 비교한다.
  [343434, 333, 303030]이 되고, 따라서 최종 정렬 순서는 [9, 5, 34, 3, 30]이 된다.
  즉 x*3의 과정은 원소 길이를 맞춰 비교하기 위해서 늘려주는 것이라 이해하면 된다.
  
  ### 출처
  [프로그래머스 다른 사람의 풀이](https://school.programmers.co.kr/learn/courses/30/lessons/42746/solution_groups?language=python3)

  ## 회고
  
  로직 자체는 간단해보였지만 단순하게 풀기 위해서는 꼼수가 필요했고,  
  정석대로 풀기 위해서는 functools.cmp_to_key 함수의 내부로직을 이해해야 풀 수 있는 문제였다.  
  꼼수는... 창의력의 영역이고.. 정석대로 풀려면 적절한 함수를 알아야 하기 때문에...
  좀 더 알고리즘의 영역에 공부가 필요하다고 느꼈다..
  많이 풀면... 창의력도 늘 수 있을까?..

</details>
<br>
<span style="color:gray"> #정렬 </span>
