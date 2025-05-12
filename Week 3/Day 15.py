print("\n\nDay 15\n")

print("\nChallenge (FACEprep): Count Odd Numbers in an Interval Range")
print("Context: Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).\n\n")

class Odd:
    def countOdds(self, low: int, high: int) -> int:
        total_numbers = high - low + 1
        if total_numbers % 2 == 0:
            return total_numbers // 2
        else:
            return (total_numbers + 1) // 2 if low % 2 == 1 else total_numbers // 2

solution = Odd()
low = 3
high = 7
result = solution.countOdds(low, high)
print(f"The number of odd numbers between {low} and {high} (inclusive) is: {result}")