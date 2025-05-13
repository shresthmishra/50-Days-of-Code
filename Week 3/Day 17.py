print("\n\nDay 17\n")

print("\nChallenge (FACEprep): Reverse Integer")
print("Context: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.\n\n")

class Reversal:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        reversed_num *= sign
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num

solution = Reversal()
number = 754
reversed_integer = solution.reverse(number)
print(f"The reverse of {number} is: {reversed_integer}")