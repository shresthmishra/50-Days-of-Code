print("\n\nDay 49\n")

print("\nChallenge: Prime Number of Set Bits in Binary Representation")
print('''Context: Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

    For example, 21 written in binary is 10101, which has 3 set bits.\n\n
''')

class Prime:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        count = 0
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if set_bits in primes:
                count += 1
        return count

solution = Prime()
left_val = 6
right_val = 10
result = solution.countPrimeSetBits(left_val, right_val)
print(f"The count of numbers with a prime number of set bits between {left_val} and {right_val} is: {result}")
