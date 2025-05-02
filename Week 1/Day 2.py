print("\n\nDay 2\n")

print("Challenge (GeeksforGeeks): Move All Zeroes to End")
print("Context: You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.\n")

class Zeroes:
    def pushZerosToEnd(self, arr):
        non_zero_pos = 0
        for i in range(len(arr)):
            if int(arr[i]) != 0:
                arr[non_zero_pos], arr[i] = arr[i], arr[non_zero_pos]
                non_zero_pos += 1
solution = Zeroes()
my_array = [1, 2, 0, 4, 3, 0, 5, 0]
solution.pushZerosToEnd(my_array)
print(f"Array after pushing zeros to the end: {my_array}")