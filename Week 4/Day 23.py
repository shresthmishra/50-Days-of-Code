print("\n\nDay 23\n")

print("\nChallenge: Find Greatest Common Divisor of Array")
print("Context: Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums. \nThe greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.\n\n")

from typing import List

class Greatest:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
    
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        return gcd(min_num, max_num)

solution = Greatest()
numbers = [2, 5, 6, 9, 10]
result = solution.findGCD(numbers)
print(f"The greatest common divisor of the smallest and largest numbers in {numbers} is: {result}")
