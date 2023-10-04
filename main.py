from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}  # 딕셔너리를 사용하여 숫자와 인덱스를 저장
    
    for i, num in enumerate(nums):
        complement = target - num 
        
        # 보수가 딕셔너리에 있으면 해당 보수의 인덱스와 현재 인덱스 반환
        if complement in num_dict:
            return [num_dict[complement], i] 
        
        # 현재 숫자를 딕셔너리에 저장
        num_dict[num] = i

    return []
