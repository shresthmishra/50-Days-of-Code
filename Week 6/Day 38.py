print("\n\nDay 38\n")

print("\nChallenge: Number of Segments in a String")
print("Context: Given a string s, return the number of segments in the string.\nA segment is defined to be a contiguous sequence of non-space characters.\n\n")

class Segments:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        
solution = Segments()
s = "Hello, my name is Shresth."
result = solution.countSegments(s)
print(f"Number of the segments in the string s is {result}")