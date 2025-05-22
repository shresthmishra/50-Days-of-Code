print("\n\nDay 26\n")

print("\nChallenge: Search Insert Position")
print("Context: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.\nYou must write an algorithm with O(log n) runtime complexity.\n\n")

from typing import List

class InsertPosition:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

# Sample Usage
solution = InsertPosition()
numbers = [1, 3, 5, 6]
target_value = 5
insert_index = solution.searchInsert(numbers, target_value)
print(f"For nums = {numbers} and target = {target_value}, the insert index is: {insert_index}")