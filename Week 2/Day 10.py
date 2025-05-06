print("\n\nDay 10\n")

print("\nChallenge (FACEprep): Plus One")
print("Context: You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. \nIncrement the large integer by one and return the resulting array of digits.\n\n")

class PlusOne:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

solution = PlusOne()
number_digits = [1, 2, 3]
result = solution.plusOne(number_digits)
print(f"Original digits: {number_digits}, Result after plus one: {result}")

number_digits_at_nine = [9, 9, 9]
result_at_nine = solution.plusOne(number_digits_at_nine)
print(f"Original digits: {number_digits_at_nine}, Result after plus one: {result_at_nine}")