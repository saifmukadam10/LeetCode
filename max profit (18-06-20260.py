class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Edge case: If there are fewer than 2 days, no transaction can be made
        if not prices or len(prices) < 2:
            return 0
        
        # Track the minimum price seen so far and the maximum profit
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # If we find a lower buying price, update min_price
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today yields a higher profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
    
prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
# time complexity: O(n)
# space complexity: O(1)