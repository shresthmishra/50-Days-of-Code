print("\n\nDay 39\n")

print("\nChallenge: Reverse Vowels of a String")
print("Context: Given a string s, reverse only all the vowels in the string and return it.\nThe vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.\n\n")

class Vowels:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            
        return ''.join(s_list)

solution = Vowels()
input_string = "June"
result = solution.reverseVowels(input_string)
print(f"Original string: '{input_string}'")
print(f"String with reversed vowels: '{result}'")
