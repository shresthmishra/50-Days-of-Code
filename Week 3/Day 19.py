print("\n\nDay 19\n")

print("\nChallenge (FACEprep): Sum of Square Numbers")
print("Context: Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.\n\n")

class Square:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        
        while left <= right:
            curr_sum = left * left + right * right
            if curr_sum == c:
                return True
            elif curr_sum < c:
                left += 1
            else:
                right -= 1
        return False

solution = Square()
number = 5
result = solution.judgeSquareSum(number)
print(f"Can {number} be expressed as the sum of two squares? {result}")
