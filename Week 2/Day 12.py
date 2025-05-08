print("\n\nDay 12\n")

print("\nChallenge (FACEprep): Nth Digit")
print("Context: Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].\n\n")

class Nth:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        number = start + (n - 1) // length
        digit_position = (n - 1) % length
        return int(str(number)[digit_position])

solution = Nth()
n_value = 3
result = solution.findNthDigit(n_value)
print(f"The {n_value}th digit is: {result}")
