print("\n\nDay 42\n")

print("\nChallenge: Remove All Adjacent Duplicates In String")
print("Context: You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.\nWe repeatedly make duplicate removals on s until we no longer can.\nReturn the final string after all such duplicate removals have been made. It can be proven that the answer is unique.\n\n")

class Duplicates:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

solution = Duplicates()
input_string = "abbaca"
result = solution.removeDuplicates(input_string)
print(f"Original string: '{input_string}'")
print(f"String after removing adjacent duplicates: '{result}'")
