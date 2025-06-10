print("\n\nDay 45\n")

print("\nChallenge: Reverse Words in a String")
print("Context: Given an input string s, reverse the order of the words.\nA word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.\nReturn a string of the words in reverse order concatenated by a single space.\nNote that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.\n\n")

class Reverse:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)

solution = Reverse()
string = "Earth is pretty"
result = solution.reverseWords(string)
print(f"The string given as input: {string}")
print(f"The Reversed String is: {result}")