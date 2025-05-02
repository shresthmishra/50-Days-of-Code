print("\n\nDay 3\n")

print("Challenge (GeekforGeeks): Second Largest")
print("Context: Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.\n")

class SecondLargest:
    def getSecondLargest(self, arr):
        if not arr or len(arr) < 2:
            return -1
        unique_elements = sorted(list(set(arr)), reverse=True)
        if len(unique_elements) < 2:
            return -1
        else:
            return unique_elements[1]
solution = SecondLargest()
numbers = [2, 5, 4, 3, 7]
second_largest = solution.getSecondLargest(numbers)
print(f"The second largest element in {numbers} is: {second_largest}")