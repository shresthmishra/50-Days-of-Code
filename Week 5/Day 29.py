print("\n\nDay 29\n")

print("\nChallenge: Find First and Last Position of Element in Sorted Array")
print("Context: Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.\nIf target is not found in the array, return [-1, -1].\nYou must write an algorithm with O(log n) runtime complexity.\n\n")

from typing import List

class FirstandLast:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, left_bias):
            left, right = 0, len(nums) - 1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    i = mid
                    if left_bias:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i
        left_index = binary_search(nums, target, True)
        right_index = binary_search(nums, target, False)
        return [left_index, right_index]

solution = FirstandLast()
numbers = [5, 7, 7, 8, 8, 10]
target = 8
result = solution.searchRange(numbers, target)
print(f"For nums = {numbers}, target = {target}, the range is: {result}")
