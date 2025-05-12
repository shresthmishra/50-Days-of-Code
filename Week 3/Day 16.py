print("\n\nDay 16\n")

print("\nChallenge (FACEprep): Sign of the Product of an Array")
print("Context: Implement a function signFunc(x) that returns:\n- 1 if x is positive.\n- -1 if x is negative.\n- 0 if x is equal to 0.\nYou are given an integer array nums. Let product be the product of all values in the array nums.\nReturn signFunc(product).\n\n")

from typing import List

class Sign:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign
        return sign

solution = Sign()
nums1 = [-1, -2, -3, 4]
result1 = solution.arraySign(nums1)
print(f"The sign of the product of {nums1} is: {result1}")

nums2 = [-1, 2, -3, -4]
result2 = solution.arraySign(nums2)
print(f"The sign of the product of {nums2} is: {result2}")