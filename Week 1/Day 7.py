print("\n\nDay 7\n")

print("\nChallenge: Check if the number is Palindrome")
class Palindrome:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        return str_x == str_x[::-1]
solution = Palindrome()
number = 121
result = solution.isPalindrome(number)
print(f"Is {number} a palindrome? {result}")