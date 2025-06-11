print("\n\nDay 46\n")

print("\nChallenge: Zigzag Conversion")
print('''Context: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
''')

class Zigzag:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        step = 1
        row = 0
        for char in s:
            rows[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(rows)

solution = Zigzag()
input_string = "PAYPALISHIRING"
num_rows = 3
converted_string = solution.convert(input_string, num_rows)
print(f"The string '{input_string}' converted with {num_rows} rows is: '{converted_string}'")

    
