print("\n\nDay 19\n")

print("\nChallenge: Contains Duplicate")
print("Context: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.\n\n")

from typing import List

class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

solution = ContainsDuplicate()
numbers = [1, 2, 3, 1]
result = solution.containsDuplicate(numbers)
print(f"Does the list contain any duplicate? {result}")