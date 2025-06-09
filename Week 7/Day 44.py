print("\n\nDay 44\n")

print("\nChallenge: Longest Common Prefix")
print("Context: Write a function to find the longest common prefix string amongst an array of strings.\nIf there is no common prefix, return an empty string.\n\n")

from typing import List

class Prefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            char = strs[0][i]
            if any(s[i] != char for s in strs[1:]):
                return strs[0][:i]
        return strs[0][:min_len]

solution = Prefix()
input_strings = ["flower", "flow", "flight"]
lcp = solution.longestCommonPrefix(input_strings)
print(f"The longest common prefix for {input_strings} is: '{lcp}'")