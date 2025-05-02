print("\n\nDay 4\n")

print("\nChallenge 1 (LeetCode): Find Numbers with Even Number of Digits")

class EvenDigits:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
solution = EvenDigits()
nums = [1, 22, 333, 4444, 55555]
result = solution.findNumbers(nums)
print(f"Total count of numbers with even digit length: {result}")

print("\nChallenge 2 (FACEprep): Find the Missing Number in the Range")

class MissingNum:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
missing_num = MissingNum()
nums = [3, 0, 1]
result = missing_num.missingNumber(nums)
print(f"The missing number is: {result}")