print("\n\nDay 50\n")

print("\nChallenge: Number of 1 Bits")
print("Context: Given a positive integer n, write a function that returns the number of in its binary representation (also known as the Hamming weight).")

class Hammer:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

solution = Hammer()
input_n = 11  # Binary: 1011, expected 1-bits: 3
result = solution.hammingWeight(input_n)
print(f"The number of 1 bits in {input_n} is: {result}")

print("\n\nCheers to this journey! Have a good one.")