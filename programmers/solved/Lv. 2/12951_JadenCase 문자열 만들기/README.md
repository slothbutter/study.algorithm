
# [✔️][Lv. 2] [12951. JadenCase 문자열 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3)


문제 설명
-----

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)  

문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

### 제한 조건

* s는 길이 1 이상 200 이하인 문자열입니다.
* s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
  + 숫자는 단어의 첫 문자로만 나옵니다.
  + 숫자로만 이루어진 단어는 없습니다.
  + 공백문자가 연속해서 나올 수 있습니다.

### 입출력 예

| s | return |
| --- | --- |
| "3people unFollowed me" | "3people Unfollowed Me" |
| "for the last week" | "For The Last Week" |

---

※ 공지 - 2022년 1월 14일 제한 조건과 테스트 케이스가 추가되었습니다.



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```python
  def solution(s):
    words = []
    for w in s.split(" "):
        if w == "":
            words.append("")
        elif not w[0].isdigit():
            words.append(w[0].upper() + w[1:].lower())
        else:
            words.append(w[0] + w[1:].lower())
    return ' '.join(words)
  ```

  ### 1차 시도

  ```python
  def solution(s):
    return ' '.join([w[0].upper() + w[1:].lower() if not w[0].isdigit() else w[0] + w[1:].lower() for w in s.split(" ")])
  ```

  1. 단어 별로 나눠야 하므로 공백 기준으로 split을 진행
  2. 각 단어의 첫 문자를 확인하고 첫 문자가 숫자면 첫 문자를 그대로 놔두고 이후 문자를 모두 소문자로 바꾸고 리스트에 저장
  3. 첫 문자가 숫자가 아니라 영문자면 대문자로 치환하고 이후 문자를 모두 소문자로 바꾸고 리스트에 저장
  4. 단어 구분을 띄어 쓰기로 해야하므로 join할 때 사이에 들어갈 문자로 공백 추가

  ---

  <div align=center>
    <img width="963" alt="Untitle" src="https://github.com/user-attachments/assets/07a33fbb-c27e-4469-9a45-357d3891a7db"/ >
  </div>
  
  <br>
  런타임 에러의 이유는 공백이 연속해서 나올 수 있으므로 연속된 공백이 문제라고 생각했다.<br>
  프로그래머스 질문하기 란에서 답을 찾을 수 있었다. 문제는 역시 공백이었다.<br>
  공백이면 문자가 1문자밖에 존재하지 않으므로 slicing을 진행하면 에러가 발생한다.<br>
  이후 과제는 처음 나온 공백을 어떻게 처리해야하는가, 연속된 공백을 어떻게 처리해야하는가이다.

  ### 2차 시도

  ```python
  def solution(s):
    words = []
    for w in s.split(" "):
        if w == "":
            words.append("")
        elif not w[0].isdigit():
            words.append(w[0].upper() + w[1:].lower())
        else:
            words.append(w[0] + w[1:].lower())
    return ' '.join(words)
  ```

  1. 단어별로 나눠야 하므로 공백기준으로 split 진행 단, 조건에 따라 words에 넣는 값이 다름
     1. str.split(" ")로 분할 했을 때 공백이 있을 때 "" 값이 리스트에 들어감 -> str.split()으로 분할하면 단어만 남고 공백 자체는 모두 사라짐
     2. 공백을 표시해주기 위해서 해당 값은 처리해주지 않고 words에 그대로 넣음
  2. 단어의 처음이 숫자가 아니면 처음을 대문자로 바꾸고 이후는 소문자로 바꾼 뒤 words에 넣음
  3. 숫자일때는 처음 문자는 그대로 놔두고 이후 문자를 소문자로 바꿈 -> 이는 숫자가 첫 문자에서만 나올 수 있다는 조건 때문에 성립한다.
  4. 이후 words를 string화 할 때 구분자로 공백을 넣어야 하므로 join할 때 사이에 들어갈 문자로 공백을 추가한다. -> words에 ""인 값이 존재할 때 이 또한 join을 통해 합치므로 구분자인 공백으로 변환된다.

  <div align=center>
    <img width="963" alt="Untitle" src="https://github.com/user-attachments/assets/ca5dd726-9fbe-47c5-80b1-5e15ec06d0a5" /> 
  </div>

  ### 풀이에 대한 고찰

  string은 중간 요소를 변환할 수 없으므로 단어 기준으로 split 후 join을 통해 합친다는 발상이 가능하다면 빠른 풀이가 가능하다.<br>
  단, 복기하면서 깨달은 점으로 string.split()은 default로 모든 공백 문자(스페이스, 탭, 개행 등)를 분할자로 사용한다는 것이다.<br>
  즉, string.split(" ")이 아닌 string.split()을 사용했다면 앞에 공백을 표시하는 ""(빈 문자열)이 words의 요소에 포함되지 않는다.

  ## 다른 사람 풀이

  ### 코드
  ```python
  # 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
  # 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
  def Jaden_Case(s):
      # 함수를 완성하세요
      return s.title()

  # 아래는 테스트로 출력해 보기 위한 코드입니다.
  print(Jaden_Case("3people unFollowed me for the last week"))
  ```
  ### 설명
  문제가 개편되기 전의 코드이다. 위 코드를 동작시키면 "3People Unfollowed Me"이 출력된다.<br>
  string.title()은 내장 문자열 메서드 중 하나이며 문자열의 첫 문자는 무조건 대문자로 변환하고, cased하지 않은 문자(대/소문자 구분이 없는)를 기준으로 다음 문자를 대문자로 변환하는 메서드이다. <br>
  위의 결과를 보면 첫 문자는 무조건 대문자이지만 3은 cased하지 않은 문자이다. 따라서 그 다음 문자인 p가 대문자로 변환되어 "3People"가 된다.<br>
  하지만, 이는 개편된 문제의 조건과 부합하지 않으므로 word로 split 후 조건에 따라서 해당 word를 title화 시키는 용도로 사용할 수 있을 것으로 개선 할 수 있을 것 같다.<br>

  ### 출처
  [프로그래머스 다른 사람 풀이 1번](https://school.programmers.co.kr/learn/courses/30/lessons/12951/solution_groups?language=python3&type=all)

  ## 다른 사람 풀이2
  
  ### 코드
  ```python
  def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])
  ```

  ### 설명
  string.capitalize()는 내장 문자열 메서드 중 하나이며 문자열에서 첫 문자만 대문자로 변환하고 나머지 문자는 소문자로 변환하는 메서드이다.<br>
  위의 string.title()과 다른 점은 오직 첫 문자만 대문자로 변환한다는 점이다. 또한 첫 문자가 cased하지 않은 문자이면 변화가 없다.<br>
  이러한 점을 이용해서 s를 단어화 해서 각 단어별로 string.capitalize()를 적용시키면 문제에서 원하는 결과를 얻을 수 있다.

  ### 출처
  [프로그래머스 다른 사람 풀이 3번](https://school.programmers.co.kr/learn/courses/30/lessons/12951/solution_groups?language=python3&type=all)

  
  ## 회고
  string은 index를 통해 중간 요소를 변경할 수 없다는 점을 명심하고 있으면 의외로 빠르게 그리고 쉽게 풀리는 문제였다.<br>
  또한 단순하게 풀면 단순하게 풀 수 있지만 문자열에 대한 메서드를 조금 더 자세히 알고 있으면 더 효율적이게 풀 수 있었던 문제였던 것 같다.<br>
  이번에 새로 나온 string.title()과 string.capitalize()는 기억해두자!<br>
  언제 어디서 문자열에 관련된 문제가 출제될 지 모르니 말이다.

</details>
<br>
<span style="color:gray"> #문자열 </span>
