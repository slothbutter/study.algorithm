
# ✔️[Lv. 2] [12939. 최댓값과 최솟값](https://school.programmers.co.kr/learn/courses/30/lessons/12939)


문제 설명
-----

문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.  

예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

### 제한 조건

* s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

### 입출력 예

| s | return |
| --- | --- |
| "1 2 3 4" | "1 4" |
| "-1 -2 -3 -4" | "-4 -1" |
| "-1 -1" | "-1 -1" |



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```python
  def solution(s):
    return "{0} {1}".format(min(map(int, s.split())), max(map(int, s.split())))
  ```

  ---

  <div align=center>
    <img width="963" alt="Untitle" src="https://github.com/user-attachments/assets/63d61dd4-fade-463e-b06b-40ce931a673e" />
  </div>

  ### 풀이에 대한 고찰

  역시 Lv. 2이지만 정답률 80% 짜리 문제여서 그런지 어렵지 않다.<br>
  그냥 string을 공백기준으로 자르는데 각각의 원소를 int형으로 형변환해서 map(iterable)으로 만들고 min과 max를 사용해서 최대 최솟값을 구한다.<br>
  사실 위의 코드가 그리 효율적인 것은 아니다. 한 줄로 작성해보려고 저렇게 만든것이지 map을 두번이나 따로 만들 필요없이 변수에 할당하고 사용하면 된다.

  ## 다른 사람 풀이

  ### 코드
  ```python
  def solution(s):
    t = []
    if s[0] != "-":
        s = "+" + s
    for i in range(0, len(s)):
        t += [s[i]]
    for i in range(0, len(t)):
        if t[i] == " " and t[i+1] != "-":
            t.insert(i+1, "+")
    for i in range(1, len(t)):
        if t[len(t)-i] == " " and t[len(t)+1-i] != "-":
            t.insert(len(t)+1-i, "+")
            break
    print(t)
    result = []
    midcount1 = ""
    midcount2 = ""
    for i in range(len(t)):

        if t[i] == "-": 
            for j in range(i+1, len(t)):
                if t[j] != " ":
                    midcount1 = midcount1 + t[j]
                    if j == len(t)-1:
                        result += [-int(midcount1)]
                        midcount1 = ""
                        break
                elif t[j] == " ":
                    print(midcount1)
                    result += [-int(midcount1)]
                    midcount1 = ""
                    break

        elif t[i] == "+":
            for j in range(i+1, len(t)):
                if t[j] != " ":
                    midcount2 = midcount2 + t[j]
                    if j == len(t)-1:
                        result += [int(midcount2)]
                        midcount2 = ""
                        break
                elif t[j] == " ":
                    print(midcount2)
                    result += [int(midcount2)]
                    midcount2 = ""
                    break


    print(result)
    resultmax = int(result[0])
    resultmin = int(result[0])
    for i in range(len(result)):
        if resultmax < result[i]:
            resultmax = result[i]
    for i in range(len(result)):
        if resultmin > result[i]:
            resultmin = result[i]
    return "%s %s" % (resultmin, resultmax)
  ```
  ### 설명
  
  간단한 문제에 긴 코드를 작성한게 있어서 가져왔다.<br>
  print(t) 이전 부분은 음수, 양수 구분을 위해 아무것도 없는 공백 사이에 "+"를 집어넣어주는 코드인 것 같다. 이후 부분은 숫자를 추출해서 리스트에 집어넣는 부분이다. 사실상 s.split()을 깡구현 한 것이다.<br>
  이후에는 전체 순회를 하며 크기 비교를 최댓값과 최솟값 각각 진행하여 최대값과 최소값을 찾는다.<br>
  <br>
  C를 안한지 너무 오래 돼서 str.split()이 없었을 때 문자열 처리를 어떻게 했는지 기억은 잘 안나지만, 왠지 저것보다 좀 더 효율적으로 숫자 추출이 가능할 것 같다는 생각이 든다.(확신은 없지만..)<br>
  파이썬의 입장에서는... 코드는 길고 효율은 더 안좋다..

  ### 출처
  [프로그래머스 다른 사람 풀이](https://school.programmers.co.kr/learn/courses/30/lessons/12939/solution_groups?language=python3)

  ## 회고
  
  간단한 문제였다. (사실 그냥 오늘 하루 코테 문제 안풀어서... Lv. 2 중에서 제일 쉬운거 1문제 풀었다.)<br>
  따로 배운점이라던가 느낀점은 없고 단지..... 파이썬은 신이야 파이썬은 무적이야 파이썬은 최고야...

</details>
<br>
<span style="color:gray"> #연습문제(구현) </span>
