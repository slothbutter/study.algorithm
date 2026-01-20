
# ✔️[Lv. 2] [42747. H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3)


문제 설명
-----

H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과[1](#fn1)에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 `n`편 중, `h`번 이상 인용된 논문이 `h`편 이상이고 나머지 논문이 h번 이하 인용되었다면 `h`의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

* 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
* 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

### 입출력 예

| citations | return |
| --- | --- |
| [3, 0, 6, 1, 5] | 3 |

### 입출력 예 설명

이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

### 문제가 잘 안풀린다면😢

힌트가 필요한가요? [코딩테스트 연습 힌트 모음집]으로 오세요! → [클릭](https://school.programmers.co.kr/learn/courses/14743?itm_content=lesson42747)

※ 공지 - 2019년 2월 28일 테스트 케이스가 추가되었습니다.

---

1. <https://en.wikipedia.org/wiki/H-index> "위키백과" [↩](#fnref1)



<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```python
  # 자기를 포함해서 앞에 있는 것 개수만 세서 하면 되는거 아닌가?
  def solution(citations):
      citations = sorted(citations, reverse=True)
      h_index = -1
      # h = 인용 수, i+1 = 자신(포함)보다 인용 수가 많은 논문의 수
      for i, h in enumerate(citations):
          h_index = max(h_index, min(i+1, h))
      return h_index
  ```

  <img width="969" height="535" alt="image" src="https://github.com/user-attachments/assets/bb981666-8467-49bd-ba75-fc5590499a65" />

  ### 풀이에 대한 고찰
  문제에서 h-index의 조건이 h번 이상 인용된 논문이 h편 이상인 h의 최댓값이 h-index라고 했으니  
  해당 문제를 풀기 위해서는 두 가지 정보가 필요하다.  
  
  1. 자신을 포함해서 인용수가 더 많은 논문의 수
  2. 자신의 인용수  
  
  1번 정보를 얻기 위해 citations를 내림차순 정렬하여 citations의 index를 자신보다 인용수가 많은 논문의 개수로 설정한다.
  2번 정보는 citations의 값으로 들어가있다.

  이제 이를 조합하여 문제를 풀어보자.  
  만약 citations=[32, 31, 30]이라고 해보자  
  citations[0]인 32는 h-index가 될 수 있는 후보군인 h값은 32번 이상 인용된 논문이 1편 있으므로 1 밖에 존재하지 않을 것이다.  
  마찬가지로 citations[1]인 31의 h값은 31번 이상 인용된 논문이 2편 존재하므로 [1, 2]이다.  
  이 때, h의 최대값이 h-index이므로 h-index는 2이다.  
  이를 알고리즘으로 적으면 자신(포함)보다 인용수가 많은 논문의 수(citations의 index + 1)과 자신의 인용수(citations의 값) 중 작은 값이 해당 시점에서의 h-index가 된다.  
  <br>
  반대로 자신을 포함한 인용수가 더 많은 논문의 수가 자신의 인용 수 보다 많으면 어떻게 될까?  
  citations=[2, 2, 2]라고 해보자  
  citations[0]의 시점에서는 2인 h-index가 될 수 있는 후보군인 h값은 2번 이상 인용된 논문이 1편 있으므로 1 밖에 존재하지 않는다.  
  그렇다면 citations[2]의 시점에서는 2번 이상 인용된 논문이 3편 존재하지만, h값은 서로 동일한 값까지만 가능하기 때문에 [1, 2]가 h-index의 후보군이 된다.  
  <br>
  한 값을 검증할 때마다 시점이 계속 바뀌기 때문에 해당 시점에서 최대값을 h-index로 설정하면 문제에서 요구하는 h-index를 구할 수 있다.
  
  ## 다른 사람 풀이

  ### 코드1
  ```python
    def solution(citations):
    sorted_citations = sorted(citations, reverse=True)
    for i in range(len(sorted_citations)):
        if sorted_citations[i] <= i: 
            return i
    return len(sorted_citations)
  ```
  ### 설명
  정석대로의 풀이  
  나의 정답코드와 로직은 비슷하지만 더 효율적인 방법을 사용했다.  
  당장의 나의 코드에서는 index를 비교하기 위해서 enumerate()를 추가적으로 사용했다.  
  값을 비교하는 부분에서 어차피 내림차순으로 정렬이 되어있으므로 해당 index는 자신보다 인용이 더 많이 된 논문의 수이다.  
  또한, h값은 해당 논문의 인용수를 넘을 수 없기 때문에 i값보다 인용수가 작아지는 경우가 오면 최대 h값은 i로 고정된다.  
  따라서, citations의 값이 i보다 낮거나 같아지는 지점이 있으면 해당 값이 h-index이고,  
  전체 순회를 해도 위 조건을 만족하는 i값이 없으면 논문의 개수가 h-index가 된다.

  ### 코드2
  ```python
    def solution(citations):
        citations.sort(reverse=True)
        answer = max(map(min, enumerate(citations, start=1)))
        return answer
  ```

  ### 설명
  내가 풀었던 방식과 완전히 똑같은 방식의 풀이이다.  
  다만 코드 라인 수를 줄이기위해 map을 사용하였다.  
  코드가 깔끔해보이긴 하지만 가독성 측면에서 별로 좋지 못하다고 생각한다.  
  일부 의견중에서는 코드1보다 시간복잡도가 더 크다 혹은 효율성이 떨어진다는 의견도 있다.

  ### 출처
  [프로그래머스 다른사람의 풀이](https://school.programmers.co.kr/learn/courses/30/lessons/42747/solution_groups?language=python3)

  ## 회고
  사실 해당 문제는 이틀에 걸쳐서 풀었다.  
  첫 날에는 GPT를 통해 힌트를 받고 풀었다.  
  힌트를 보니 깨달은 것이 h-index에 대해서 문제가 너무 장황하게 설명하고 있다는 점이있다.  
  단순히 "h번 이상 인용된 논문이 h편 이상인 h의 최댓값이 h-index"라고 설명을 했더라면 좀 더 수월하게 풀 수 있었을 것 같다.

</details>
<br>
<span style="color:gray"> #정렬 </span>
