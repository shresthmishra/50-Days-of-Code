print("\n\nDay 47\n")

print("\nChallenge: Maximum Number of Vowels in a Substring of Given Length")
print("Context: Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.\nVowel letters in English are 'a', 'e', 'i', 'o', and 'u'.\n\n")

class Max:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        curr_count = sum(1 for i in range(k) if s[i] in vowels)
        max_count = curr_count
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_count += 1
            if s[i - k] in vowels:
                curr_count -= 1
            max_count = max(max_count, curr_count)
        
        return max_count

solution = Max()
s_val = "abciiidef"
k_val = 3
result = solution.maxVowels(s_val, k_val)
print(f"For string '{s_val}' and length {k_val}, the maximum number of vowels is: {result}")