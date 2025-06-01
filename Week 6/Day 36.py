print("\n\nDay 36\n")

print("\nChallenge: Lexicographically Smallest Palindrome")
print("Context: You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.\n- Your task is to make s a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.\n- A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.\n- Return the resulting palindrome string.\n\n")

class Palindrome:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s_list[left] != s_list[right]:
                if s_list[left] < s_list[right]:
                    s_list[right] = s_list[left]
                else:
                    s_list[left] = s_list[right]
            left += 1
            right -= 1
        return ''.join(s_list)

solution = Palindrome()
input_string = "egcfe"
result = solution.makeSmallestPalindrome(input_string)
print(f"The smallest lexicographical palindrome for '{input_string}' is: '{result}'")