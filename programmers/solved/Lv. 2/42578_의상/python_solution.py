from collections import Counter
from functools import reduce
from math import prod
def solution(clothes):
    _, category = zip(*clothes)
    cnt = Counter(category)
    answer = reduce(lambda x, y: (x+1) * (y+1) - 1, cnt.values())
    # answer = reduce(lambda x, y: x * (y+1), cnt.values(), 1) - 1 #초기값을 지정하지 않으면 x에 이미 값이 들어가서 사용되기 때문에 정답보다 값이 작아짐
    # answer = prod([value + 1 for value in cnt.values()]) - 1
    return answer      
    
if __name__ == "__main__":
    clothes_list =[
        [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    ]
    result = [5, 3]
    
    for i, clothes in enumerate(clothes_list):
        if result[i] == solution(clothes):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(clothes)}이 기댓값 {result[i]}과 다릅니다.")
        