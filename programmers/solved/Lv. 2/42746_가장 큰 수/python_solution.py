from functools import cmp_to_key
def solution(numbers):
    def sort_condition(a, b):
        if a+b > b+a:
            return -1
        elif a+b < b+a:
            return 1
        else:
            return 0
    numbers = list(map(str, numbers))
    sorted_numbers = sorted(numbers, key=cmp_to_key(sort_condition))
    result = ''.join(sorted_numbers)
    if int(result) == 0:
        return '0'
    else:
        return result    
    
if __name__ == "__main__":
    n_list =[[6, 10, 2], [3, 30, 34, 5, 9], [0, 0, 0]]
    result = ["6210", "9534330", "0"]
    
    for i, n in enumerate(n_list):
        if result[i] == solution(n):
            print("테스트를 통과하였습니다.")
        else:
            print(f"실행한 결괏값 {solution(n)}이 기댓값 {result[i]}과 다릅니다.")
        