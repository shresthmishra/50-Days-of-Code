print("\n\nDay 18\n")

print("\nChallenge (FACEprep): Excel Sheet Column Title")
print("Context: Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.\n\n")

class Excel:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            digit = columnNumber % 26
            result = chr(ord('A') + digit) + result
            columnNumber //= 26
        return result

solution = Excel()
column_number = 28
excel_title = solution.convertToTitle(column_number)
print(f"The Excel column title for {column_number} is: {excel_title}")
