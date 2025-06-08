print("\n\nDay 43\n")

print("\nChallenge: Rotate String")
print("Context: Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.\nA shift on s consists of moving the leftmost character of s to the rightmost position.\nFor example, if s = 'abcde', then it will be 'bcdea' after one shift.\n\n")

class Rotate:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)

solution = Rotate()
s_1 = "abcdef"
goal_1 = "defabc"
s_2 = "shresth"
goal_2 = "esthshr"
result1 = solution.rotateString(s_1, goal_1)
result2 = solution.rotateString(s_2, goal_2)
print(f"Can '{s_1}' be rotated to '{goal_1}'? {result1}")
print(f"Can '{s_2}' be rotated to '{goal_2}'? {result2}")