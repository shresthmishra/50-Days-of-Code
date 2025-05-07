print("\n\nDay 11\n")

print("\nChallenge (FACEprep): Excel Sheet Column Number")
print("Context: Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.\n\n")

class Excel:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result *= 26
            result += ord(char) - ord('A') + 1
        return result

solution = Excel()
column = "AB"
number = solution.titleToNumber(column)
print(f"The Excel column title '{column}' corresponds to the number: {number}")

column2 = "ZY"
number2 = solution.titleToNumber(column2)
print(f"The Excel column title '{column2}' corresponds to the number: {number2}")