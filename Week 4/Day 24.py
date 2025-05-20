print("\n\nDay 24\n")

print("\nChallenge: Pascal's Triangle II")
print("Context: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.\n\n")

from typing import List

class Pascal:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j-1]
        
        return row

solution = Pascal()
row_index = 3
pascal_row = solution.getRow(row_index)
print(f"The {row_index}th row of Pascal's Triangle is: {pascal_row}")
