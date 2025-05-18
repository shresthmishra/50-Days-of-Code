print("\n\nDay 22\n")

print("\nChallenge: Best Time to Buy and Sell Stock")
print("Context: You are given an array prices where prices[i] is the price of a given stock on the ith day.\nYou want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\nReturn the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.\n\n")
      
from typing import List

class Stocks:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)
        return max_profit
    
solution = Stocks()
prices = [7, 1, 5, 3, 6, 4]
max_profit = solution.maxProfit(prices)
print(f"For the given prices {prices}, the maximum profit is: {max_profit}")