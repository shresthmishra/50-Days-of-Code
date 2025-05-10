print("\n\nDay 14\n")

print("\nChallenge (FACEprep): Factorial Trailing Zeroes")
print("Context: Given an integer n, return the number of trailing zeroes in n!.\n\n")

class Trailer:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

solution = Trailer()
number = 3
result = solution.trailingZeroes(number)
print(f"The number of trailing zeroes in factorial of {number} is: {result}")

number2 = 5
result2 = solution.trailingZeroes(number2)
print(f"The number of trailing zeroes in factorial of {number2} is: {result2}")

number3 = 30
result3 = solution.trailingZeroes(number3)
print(f"The number of trailing zeroes in factorial of {number3} is: {result3}")