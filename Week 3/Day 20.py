print("\n\nDay 19\n")

print("\nChallenge: Two Sum")
print("Context: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n\n")
from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
    
solution = TwoSum()
numbers = [2, 7, 11, 15]
target_sum = 9
result = solution.twoSum(numbers, target_sum)
print(f"For nums = {numbers}, target = {target_sum}, the indices of the two numbers that add up to the target are: {result}")
