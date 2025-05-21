print("\n\nDay 25\n")

print("\nChallenge: Majority Element")
print("Context: Given an array nums of size n, return the majority element.\n\n")

from typing import List

class Major:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

solution = Major()
numbers = [3, 2, 3]
majority_element = solution.majorityElement(numbers)
print(f"The majority element in {numbers} is: {majority_element}")
