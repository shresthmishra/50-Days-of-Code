#1 Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

#2 Missing Number in the Range
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum