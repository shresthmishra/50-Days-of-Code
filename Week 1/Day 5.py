print("\n\nDay 5\n")

print("\nChallenge 1 (LeetCode): Merge Strings Alternately")

class Alternatives:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
            i += 1
        return ''.join(merged)
solution = Alternatives()
word1 = "hello"
word2 = "world"
result = solution.mergeAlternately(word1, word2)
print(f"Merged string for '{word1}' and '{word2}': {result}")

print("\nChallenge 2 (FACEprep): Add Digits")
print("Context: Repeatedly add all its digits until the result has only one digit, and return it.")

class AddDigits:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

solver = AddDigits()
sample_number = 38
result = solver.addDigits(sample_number)
print(f"Input: {sample_number}, Output: {result}")