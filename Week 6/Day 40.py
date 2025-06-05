print("\n\nDay 40\n")

print("\nChallenge: Find First Palindromic String in the Array")
print("Context: Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".\nA string is palindromic if it reads the same forward and backward.\n\n")

class FirstPalindrome:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
    
solution = FirstPalindrome()
List = ["shresth","racecar","shivam","ada"]
result = solution.firstPalindrome(List)
print(f"The First Palindromic String in the given Array is: {result}")