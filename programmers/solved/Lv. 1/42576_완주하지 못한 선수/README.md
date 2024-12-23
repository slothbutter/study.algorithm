
# ✔️[Lv. 1] [42576. 완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)


문제 설명
-----

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

### 제한사항

* 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
* completion의 길이는 participant의 길이보다 1 작습니다.
* 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
* 참가자 중에는 동명이인이 있을 수 있습니다.

### 입출력 예

| participant | completion | return |
| --- | --- | --- |
| ["leo", "kiki", "eden"] | ["eden", "kiki"] | "leo" |
| ["marina", "josipa", "nikola", "vinko", "filipa"] | ["josipa", "filipa", "marina", "nikola"] | "vinko" |
| ["mislav", "stanko", "mislav", "ana"] | ["stanko", "ana", "mislav"] | "mislav" |

### 입출력 예 설명

예제 #1  

"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2  

"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3  

"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

---

※ 공지 - 2023년 01월 25일 테스트케이스가 추가되었습니다.



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```
  (작성한 정답 코드를 게시 -> 실패하면 작성x)
  ```

  ### 1차 시도

  ```python
  def solution(participant, completion):
    for name in completion:
        participant.remove(name)
    return ''.join(participant)
  ```

  단순히 list.remove()로 값을 하나씩 제거해가며 완주자를 모두 제거했다.

  ---

  <div align=center>
  <img width="960" alt="스크린샷 2024-12-23 오전 12 14 41" src="https://github.com/user-attachments/assets/dad420ee-1ea8-447c-91d2-9a47a2164945" />
  </div>

  ### 풀이에 대한 고찰

  테스트 케이스에서는 모두 정답을 맞췄으나, 효율성 테스트에서 통과하지 못했다.  
  그 이유는 list.remove()의 시간복잡도는 O(n)이다. 따라서 리스트의 크기만큼 실행시간이 증가한다.  
  최악의 경우 문제에서 주어진 최대 리스트의 길이인 100,000을 모두 순회해야 완주자 1명을 찾을 수 있다.

  ### 2차 시도

  ```python
  from collections import Counter
  def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    decompletion = participant - completion
    return list(decompletion.keys())[0]
  ```

  collections.Counter 객채를 사용해서 참여자와 완주자의 이름의 개수를 모두 센 다음 둘을 빼서 남은 한 명의 이름을 출력했다.

  > [!NOTE]
  > **collections.Counter**(https://mein-figur.tistory.com/entry/python-collections-counter)<br>
  > <br>
  >Counter는 Python의 collections 모듈에 포함된 클래스로, 해시 가능한 객체의 개수를 쉽게 계산하고 관리할 수 있다. 리스트, 문자열, 딕셔너리 등에서 요소의 빈도를 세어 딕셔너리 형태로 반환하며, 키는 요소, 값은 빈도를 나타낸다. 주요 메서드로는 요소를 개수만큼 반복 반환하는 elements(), 빈도 순으로 정렬된 결과를 반환하는 most_common(), 요소의 개수를 줄이는 subtract() 등이 있다. 또한 덧셈, 뺄셈, 교집합, 합집합 연산도 지원해 데이터를 효율적으로 비교하거나 조합할 수 있다. 주로 데이터 분석, 빈도 계산, 중복 체크 등에 유용하게 활용가능하다. Counter는 딕셔너리 자료형(해시 테이블)을 기반으로 동작하므로 대부분의 연산은 O(n)의 시간 복잡도를 가지며, 요소 접근 및 삭제의 경우 O(1)의 시간 복잡도를 가진다.

  ---

  <div align=center>
  <img width="964" alt="스크린샷 2024-12-23 오전 12 50 46" src="https://github.com/user-attachments/assets/2a8e399f-17ed-445a-b308-604dfe7d91fe" />
  </div>

  ### 풀이에 대한 고찰

  정답! Counter 객채는 Dictionary와 같은 구조를 띄므로 key를 통해서 접근할 수 있다
  보통의 해시 테이블 기반 데이터 구조의 요소 접근은 평균적으로 O(1)이므로 Counter 객체의 더하거나 빼는 연산은 두 객체의 키의 개수에 영향을 받아 O(k)(k는 키의 개수)이다. 따라서 최악의 경우라도 99,999번만 연산하면 완주 못한 선수를 찾을 수 있다.

  ## 다른 사람 풀이


  ### 코드
  ```python
  def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
  ```
  ### 설명
  
  로직은 같으나 해시 함수를 사용해서 이름을 고유한 키로 만들고 모든 참가자 키를 더한 후 완주자 키를 빼면 완주하지 못한 사람의 해시만 남을 것이므로 해당 키 값을 통해 값(이름)을 찾을 수 있다. 이 풀이는 해시 충돌만 발생하지 않는다면 신박한(나름 정석인) 풀이방법이다.

  ### 코드
  ```python
  def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
  ```
  ### 설명
  sorting을 하면 참여자와 완주자의 정렬이 동일하게 된다는 원리를 이용한 풀이방법이다.
  반복문을 돌며 해당 인덱스의 이름이 동일하지 않으면 해당 이름을 반환하고, 그렇지 않다면 가장 마지막에 남은 참여자의 이름을 반환한다.

  ### 출처
  [프로그래머스 다른 사람 풀이](https://school.programmers.co.kr/learn/courses/30/lessons/42576/solution_groups?language=python3)

  ## 회고
  반신반의하며 첫 시도로 정말 단순하게 풀어보려했지만 역시나 시간복잡도에 걸렸다.  
  사실 시간복잡도 계산을 하지 않고 그냥 풀긴해서 그 부분을 반성해야할 것 같다.  
  list.remove()가 전체 순회를 하며 삭제할 값을 찾는다는 것을 기억하자.  
  또한 collections.Counter 객체를 더 유용하게 사용할 수 있을 것 같으니 숙지하자.

</details>
<br>
<span style="color:gray"> #해시 </span>
