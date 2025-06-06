print("\n\nDay 41\n")

print("\nChallenge: Valid Palindrome")
print("Context: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.\nGiven a string s, return true if it is a palindrome, or false otherwise.\n\n")

class Valid:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]

solution = Valid()
string = "Hello there, good people"
result = solution.isPalindrome(string)

print(f"Is the given string ''{string}'' a valid Palindrome? {result}")