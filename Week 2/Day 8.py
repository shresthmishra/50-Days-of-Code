print("\n\nDay 8\n")

print("\nChallenge (FACEprep): Perfect Square Number")
print("Context: Given a positive integer num, return true if num is a perfect square or false otherwise.\n")
class PerfectSquare:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return True

        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

solution = PerfectSquare()
number = 16
result = solution.isPerfectSquare(number)
print(f"Is {number} a perfect square? {result}")
number2 = 14
result2 = solution.isPerfectSquare(number2)
print(f"Is {number2} a perfect square? {result2}")