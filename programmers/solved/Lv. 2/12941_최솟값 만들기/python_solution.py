from functools import reduce
from math import prod
def solution(A,B):
    return reduce(lambda x, y: x + prod(y), zip(sorted(A), sorted(B, reverse=True)), 0)
    
if __name__ == "__main__":
    anb =[([1, 4, 2], [5, 4, 4]), ([1,2], [3,4])]
    result = [29, 10]
    
    for i, (A, B) in enumerate(anb):
        if result[i] == solution(A, B):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(A, B)}이 기댓값 {result[i]}과 다릅니다.")
        