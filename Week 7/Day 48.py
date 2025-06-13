print("\n\nDay 48\n")

print("\nChallenge: Greatest Common Divisor of Strings")
print("Context: For two strings s and t, we say ''t divides s'' if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).\nGiven two strings str1 and str2, return the largest string x such that x divides both str1 and str2.\n\n")

class GCS:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]

solution = GCS()
str1_val = "ABCABC"
str2_val = "ABC"
result = solution.gcdOfStrings(str1_val, str2_val)
print(f"The GCD of strings '{str1_val}' and '{str2_val}' is: '{result}'")
