print("\n\nDay 27\n")

print("\nChallenge: Move Zeroes")
print("Context: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.\nNote that you must do this in-place without making a copy of the array.\n\n")

from typing import List

class Zeroes:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1

solution = Zeroes()
numbers = [0, 1, 0, 3, 12]
print(f"Original list: {numbers}")
solution.moveZeroes(numbers)
print(f"List after moving zeros: {numbers}")