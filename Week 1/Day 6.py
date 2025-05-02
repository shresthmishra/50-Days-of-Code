print("\n\nDay 6\n")
print("\nChallenge 1 (GeeksforGeeks): Bitonic Point")
print("Context: Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array. Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.\n")

class BotanicPoint:
    def findMaximum(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return arr[left]
solution = BotanicPoint()
array = [1, 2, 4, 5, 7, 8, 3]
maximum = solution.findMaximum(array)
print(f"The maximum element in the array {array} is: {maximum}\n")

print("\nChallenge 2 (FACEprep): Perfect Number")
print("Context: A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.\n")

class Perfectionist:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        divisor_sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisor_sum += i
                if i != num // i:
                    divisor_sum += num // i
        return divisor_sum == num
solution = Perfectionist()
number = 28
result = solution.checkPerfectNumber(number)
print(f"Is {number} a perfect number? {result}")