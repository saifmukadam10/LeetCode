class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        
        # Loop through the array starting from the second day
        for i in range(1, len(prices)):
            # If the current price is higher than the previous day's price
            if prices[i] > prices[i - 1]:
                # Add the difference to our total profit
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit