print("\n\nDay 1\n")

print("Challenge: (GeeksforGeeks): Reverse an Array")

class ArrayReversal:
    def reverseArray(self, arr):
        reversedarr = arr.reverse()
        return reversedarr
solution = ArrayReversal()
my_new_array = [7,6,5,4,3,2,1]
solution.reverseArray(my_new_array)
print(f"Our new array after getting reversed: {my_new_array}")
