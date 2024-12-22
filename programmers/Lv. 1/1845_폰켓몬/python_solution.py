def solution(nums):
    select_num = len(nums) // 2
    nums = set(nums)
    if len(nums) >= select_num:
        return select_num
    else:
        return len(nums)
    
if __name__ == "__main__":
    nums =[[3, 1, 2, 3],
           [3, 3, 3, 2, 2, 4],
           [3, 3, 3, 2, 2, 2]]
    result = [2, 3, 2]
    
    for i, num in enumerate(nums):
        if result[i] == solution(num):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(num)}이 기댓값 {result[i]}과 다릅니다.")
        