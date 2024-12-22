<h1>📚 알고리즘 코드 정리</h1>

이 저장소는 알고리즘 문제를 해결하는 과정을 기록하며 회고하고자 만들어졌습니다.
<br>
<span style="color:gray">
> 본 템플릿을 사용하실 분은 template 브랜치를 fork해서 사용하시길 바랍니다.
> </span>

<h2>🎯 목표</h2>

- [ ] 백준 Silver I 달성
- [ ] 프로그래머스 순위 15000등 달성
- [ ] 프로그래머스 PCCP Lv.3 달성

<h2>🪪 프로필</h2>

<div align=center>
  
<h3>Baekjoon Tier</h3><br>

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=eastglowing)](https://solved.ac/eastglowing/) 
![mazandi profile](http://mazandi.herokuapp.com/api?handle={handle}&theme=warm)

</div>

<h2>🗂️ 디렉토리 구조</h2>

```
📂<플랫폼명>
  ┣ 📜README.md                 -> 문제 색인
  ┣ 📂Solved                    -> 풀이 성공 문제 모음
    ┣ 📂<문제 티어 또는 문제 난이도>
      ┣ 📂<문제번호_문제이름>
        ┣ 📜README.md          -> 문제 설명 및 문제 풀이
        ┣ 📜<언어_solution.언어>        -> 문제 풀이 코드
  ┣ 📂Retry                    -> 풀이 실패 문제 모음
  ┣ 📂<문제 티어 또는 문제 난이도>
    ┣ 📂<문제번호_문제이름>
      ┣ 📜README.md            -> 문제 설명 및 문제 풀이
      ┣ 📜<언어_solution.언어>          -> 문제 풀이 코드
```
<h2>📤 파일 및 커밋 규칙</h2>

- 파일 양식은 📂template의 [readme_form.md](https://github.com/godjumo/study.algorithm/blob/main/template/readme_form.md)와 [readme_example.md](https://github.com/godjumo/study.algorithm/blob/main/template/readme_example.md)를 참고하세요
- 커밋 규칙은 📂template의 [commit_template.txt](https://github.com/godjumo/study.algorithm/blob/main/commit_template.txt)을 참고하고, 적용하세요

**커밋 템플릿 적용방법**
```shell
# git 전체 commit.template 적용 (비권장)
git config --global commit.template <template의 절대경로>
# 각 프로젝트 별 commit.template 적용 (권장)
git config commit.template <프로젝트 내 template 경로>(ex ./commit_template.txt)>
```
<h2>🛠️ 사용 언어</h2>

- Python

<h2>🖊️ 문제 풀이 방법</h2>

1. **문제 이해**: 문제의 요구 사항과 제약 조건 분석
2. **풀이 계획 수립**: 제약조건 따른 알고리즘, 자료구조 선택, 시간 및 공간 복잡도 예상
3. **코드 작성 및 테스트**: 구현 및 반례 찾기
4. **풀이 과정 문서화**: 문제 설명 및 풀이 과정 문서화, 기존 코드 및 다른 풀이 코드 분석하며 주석 추가
5. **체화하기**: 손으로 알고리즘 도식화 및 풀이 방법 작성, 코드 다시 써보며 암기 및 체화

<h2>🌐 문제 풀이 플랫폼</h2>

- [백준 온라인 저지](https://www.acmicpc.net/)
- [프로그래머스](https://school.programmers.co.kr/learn/challenges?order=recent)
