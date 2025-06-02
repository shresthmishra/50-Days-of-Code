print("\n\nDay 37\n")

print("\nChallenge: Length of Last Word")
print("Context: Given a string s consisting of words and spaces, return the length of the last word in the string.\nA word is a maximal substring consisting of non-space characters only.\n\n")

class LastWord:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
solution = LastWord()
s = "I love you, mummy"
result = solution.lengthOfLastWord(s)
print(f"The Length of the Last Word of the string {s} is {result}.")