print("\n\nDay 9\n")

print("\nChallenge (FACEprep): Happy Number")
print("Context: Write an algorithm to determine if a number n is happy.\n A happy number is a number defined by the following process:\n- Starting with any positive integer, replace the number by the sum of the squares of its digits.\n- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.\n- Those numbers for which this process ends in 1 are happy.\n\n")

class Happy:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sum_squares = 0
            while n > 0:
                digit = n % 10
                sum_squares += digit * digit
                n //= 10
            n = sum_squares
        return True
    
solution = Happy()
number = 19
result = solution.isHappy(number)
print(f"Is {number} a happy number? {result}")

number2 = 2
result2 = solution.isHappy(number2)
print(f"Is {number2} a happy number? {result2}")