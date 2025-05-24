print("\n\nDay 28\n")

print("\nChallenge: Rotate Array")
print("Context: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.\n\n")

from typing import List

class Rotation:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1

solution = Rotation()

numbers = [0, 1, 0, 3, 12]
print(f"Original list: {numbers}")

solution.moveZeroes(numbers)

print(f"List after moving zeros: {numbers}")