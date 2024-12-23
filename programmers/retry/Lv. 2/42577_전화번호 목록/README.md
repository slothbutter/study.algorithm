
# ❌[Lv. 2] [42577. 전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577)


문제 설명
-----

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.  

전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

* 구조대 : 119
* 박준영 : 97 674 223
* 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone\_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

* phone\_book의 길이는 1 이상 1,000,000 이하입니다.
  + 각 전화번호의 길이는 1 이상 20 이하입니다.
  + 같은 전화번호가 중복해서 들어있지 않습니다.

### 입출력 예제

| phone\_book | return |
| --- | --- |
| ["119", "97674223", "1195524421"] | false |
| ["123","456","789"] | true |
| ["12","123","1235","567","88"] | false |

### 입출력 예 설명

입출력 예 #1  

앞에서 설명한 예와 같습니다.

입출력 예 #2  

한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3  

첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

---

**알림**

2021년 3월 4일, 테스트 케이스가 변경되었습니다. 이로 인해 이전에 통과하던 코드가 더 이상 통과하지 않을 수 있습니다.



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```
  (작성한 정답 코드를 게시 -> 실패하면 작성x)
  ```

  ### 1차 시도

  ```python
  import re

  def solution(phone_book):
    for i, num in enumerate(phone_book):
        for num2 in phone_book[i+1:]:
            if re.search(num, num2):
                return False
    return True
  ```

  정규표현식을 통해서 순회하며 접두사가 되는 경우가 있다면 바로 False를 출력하고, 끝까지 탐색해서 접두사가 나타나지 않으면 True를 출력

  ---

<br>

<div align=center>
  <img width="964" alt="스크린샷 2024-12-23 오후 9 05 01" src="https://github.com/user-attachments/assets/a5900d6b-77dc-4353-83d4-253e84e211f9" />
</div>

  ### 풀이에 대한 고찰
  
<div align=center>
  <img width="945" alt="스크린샷 2024-12-23 오후 9 12 34" src="https://github.com/user-attachments/assets/fec35872-e1a7-4151-833b-535de3a51c87" />
</div>
<br>
  해당 풀이의 반례는 제일 끝의 전화번호는 접두사 체크를 하지 않는다는 것이다.  
  위의 반례를 보면 분명 "119"는 다른 번호의 접두사가 될 수 있지만 "119"의 위치가 제일 마지막에 존재하므로 접두사 체크를 하지 않고 넘어가 true가 반환된다.

  ### 2차 시도

  ```python
  import re

  def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for i, num in enumerate(phone_book):
        for num2 in phone_book[i+1:]:
            if re.search(num, num2):
                return False
    return True
  ```

  phone_book을 번호의 길이 만큼 ascending sorting하여 마지막 번호를 체크하지 않아도 되도록 만들었다. 번호가 더 긴 것은 더 짧은 것의 접두사가 될 수 없다는 원리를 적용했다.

  ---
<br>
<div align=center>
  <img width="969" alt="스크린샷 2024-12-23 오후 9 21 00" src="https://github.com/user-attachments/assets/f0f853b6-5be7-4d5a-b51a-aeee91ea6a3e" />
</div>

  ### 풀이에 대한 고찰

<div align=center>
  <img width="945" alt="스크린샷 2024-12-23 오후 9 29 28" src="https://github.com/user-attachments/assets/e18d0620-803a-42c3-a9c1-599a52bbec5b" />
</div>  
<br>
  
  해당 반례는 접두사가 아니라 단순히 포함되어있는 관계임에도 접두사로 인식했다는 것이다.  
  위 반례를 보면 "119"는 "4376...119"의 접두사가 될 수 없음에도 불구하고 단순히 뒤에 "119"가 존재하는 것만으로도 접두사로 인식하고 false가 반환된다.  
  따라서 단순히 포함관계를 탐색하는 re.search()를 사용하는 방법보다는 다른 방법이 필요하다.

  ### 3차 시도

  ```python
  def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    
    for i, num in enumerate(phone_book):
        for num2 in phone_book[i+1:]:
            if num == num2[:len(num)]:
                return False
    return True
  ```

  번호의 길이로 ascending sorting을 진행 후 슬라이싱을 통해 그 만큼의 앞자리만 비교하고 같으면 false, 끝까지 검사 후 같은 것이 없으면 true를 반환한다.

  ---
  <br>
  <div align=center>
    <img width="962" alt="스크린샷 2024-12-23 오후 9 43 26" src="https://github.com/user-attachments/assets/16778a05-1ccf-414a-b629-e2b547844876" />
  </div>

  문제는 모두 통과했지만 시간초과가 발생한다. 아마 이중 for문 때문일 것으로 추측된다.  
  다른 방법을 찾아야한다.

  ## 다른 사람 풀이

  제한 시간안의 풀이 실패... 문제를 검색해봤다.

  ### 코드
  ```python
  def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
  ```

  ### 설명
  예전에 내가 풀었던 방식이랑 비슷하다... (실력이.. 퇴화했나?!)  
  이중 for문 사용을 방지하기 위해 미리 sorting을 진행한다.(아마 String이라서 자동으로 글자 수 내림차순이 되는 것 같다..)  
  탐색 기준이 되는 번호의 다음 번호를 기준 번호의 길이 만큼 자르고 비교한다.  
  정렬이 되어있기 때문에 기준 이전 번호는 접두사가 될 수 없다.

  ### 코드2
  ```python
  def solution(phone_book): 

    # 1.Hash map생성
    hash_map = {} 
    for nums in phone_book: 
        hash_map[nums] = 1 
    
    # 2.접두어가 Hash map에 존재하는지 찾기 
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
    
            # 3. 본인 자체일 경우는 제외
            if arr in hash_map and arr != nums:       
                return False 
                
    return True
  ```

  ### 설명
  정석인 해시맵으로 풀은 코드이다.  
  먼저 해시맵(딕셔너리)를 번호를 key로 값을 1로(자기 자신이 있기 때문) 설정하고 생성한다.  
  해당 nums를 하나씩 때어 내서 한 문자씩 조립하며 해당 해시맵에 존재하는지 확인한다.  
  예를 들어 nums가 '1234'라면 처음에는 arr에 '1'이 들어가므로 '1'이 해시맵에 존재하는지 검증한다.  
  그 후 '2'를 arr에 더하므로 '12'가 해시맵에 존재하는지 검증한다. 그리고 이를 반복한다.  
  arr이 nums와 같으면 자기자신이므로 이를 제외하고 체크 시 존재하면 false를 반환하고, 모두 검증하면 true를 반환한다.

  ### 코드3
  ```python
  def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
  ```

  ### 설명
  먼저 길이순으로 내림차순을 한다. 이유는 위와 동일하다.  
  zip 함수를 통해 기준 번호와 다음 번호를 묶어준다.  
  (zip은 빈 원소가 없게 묶인다. 즉, phone_book이 ["12", "123", "1234"]이더라도 [("12", "123"), ("123", "1234"), ("1234", "")]가 되지 않고 [("12", "123"), ("123", "1234")]로 묶인다.)  
  str.startswith()로 리스트의 앞에 해당 값이 존재하는지를 확인한다.

  > [!NOTE]
  > **파이썬 zip함수**(https://www.daleseo.com/python-zip/)<br>
  > <br>
  >zip()은 여러 iterable(리스트, 튜플 등)의 요소를 하나로 묶어주는 함수이다. iterable의 길이가 서로 다를 경우 짧은 쪽의 길이에 맞춰 짝을 지으며 결과는 튜플 형태의 iterator로 반환한다. zip(*iterable)을 통해 묶인 데이터를 다시 분리하는 것도 가능하며, 여러 그룹의 데이터를 한 번의 루프로 병렬 처리하는 곳에도 유용하게 사용할 수 있다.

  > [!NOTE]
  > **str.startswith()**(https://m.blog.naver.com/regenesis90/222387142436)<br>
  > <br>
  >startswith()는 문자열이 특정 접두사로 시작하는지 확인하는 함수이다. 확인할 문자열을 문자열이나 튜플로 전달할 수 있으며, 접두사가 존재하면 True, 존재하지 않으면 False를 반환한다. 검색 범위를 지정하고 싶다면 start와 end 매개변수를 사용하여 구간을 설정할 수 있다. 비슷한 기능으로 endswith()가 존재하며 이는 특정 접미사로 끝나는지 확인할 수 있다.

  ### 출처
  [티스토리 | [프로그래머스] 전화번호 목록 _ Python 해시Lv.**2**](https://mainkey.tistory.com/20)

  ### 코드4
  ```python
  # Trie를 이루는 노드의 구조
class TrieNode:
    def __init__(self):
        self.children = {} # {현재 번호: 다음 번호} 형식의 딕셔너리
        self.end = False # 해당 노드가 전화번호의 마지막 번호인지 여부

# Trie의 생성자와 연산
class Trie:
	# 생성자
    def __init__(self):
        self.root = TrieNode()

	# 새 전화번호를 추가하는 연산
    def insert(self, new_phone: str) -> None:
        node_now = self.root # Trie의 root부터 탐색 시작
        
        for c in new_phone: # 새 전화번호의 각 번호에 대해
            if c not in node_now.children: # 기존에 없던 번호일 경우 
                node_now.children[c] = TrieNode() # 새 노드를 만들어 갈라져나온다
            node_now = node_now.children[c] # 다음 노드로 이동
        node_now.end = True # 모든 번호에 대해 수행 후 해당 번호가 마지막 번호임을 표시

	# Trie에 저장된 번호 중 new_phone의 접두사가 있는지 찾는 연산
    def startswith(self, new_phone: str) -> bool:
        node_now = self.root # Trie의 root부터 탐색 시작

        for c in new_phone: # 새 전화번호의 각 번호에 대해
            if c not in node_now.children: # 기존 전화번호 중 접두사가 없는 경우
                return False # False 반환
            node_now = node_now.children[c] # 다음 노드로 이동
            if node_now.end: # 기존 전화번호가 끝날 때까지 새 전화번호와 일치할 경우 === 접두사
                return True # True 반환
        return True


def solution(phone_book):
    answer = True
    trie = Trie() # Trie(root) 생성

	# 각 전화번호들에 대해
    for phone_number in phone_book:
        if trie.startswith(phone_number): # Trie에 저장된 전화번호 중 접두사가 있을 경우
            return False # False 반환 후 즉시 종료
        trie.insert(phone_number) # Trie에 새 전화번호 추가

    return answer
  ```

  문자열을 탐색하는데 O(m)(m은 문자열의 길이)의 시간복잡도를 지니는 Trie 자료구조이다. 이는 문자열의 검색 속도를 빠르게 할 수 있는 자료구조이며, 검색창에 사용되는 자동 완성 기능에 Trei를 활용 할 수 있다.  

  ## 회고

  블로그 글에 따르면 Trei보다 zip을 사용한 방법이 좀 더 시간적으로나 공간적으로 효율적임을 알 수 있다...(왜???) 아마 Trie는 탐색에 시간이 조금 더 걸리는 것 같다.(하긴 문자열이 길면 더 오래 걸리니...)

  역시 Trei의 개념없이 일반화 Trei를 구현하는 것은 힘든 것 같다.. 나중에 Trei의 개념과 일반화 Trei를 따로 함께 정리해야겠다.  

  오늘 코드 정리를 했으니 시간이 좀 지난 후에 다시 풀어봐야겠다..

</details>
<br>
<span style="color:gray"> #해시 </span>
