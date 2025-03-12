
# [✔️/❌][Lv. 2] [12951. JadenCase 문자열 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3)


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

  ### 풀이에 대한 고찰

  (정답코드의 정답 이유)

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
<span style="color:gray"> #연습문제 </span>
