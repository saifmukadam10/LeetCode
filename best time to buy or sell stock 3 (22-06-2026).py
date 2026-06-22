class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        first_buy = float('inf')
        first_profit = 0
        second_buy = float('inf')
        second_profit = 0

        for i in range(len(prices)):
            first_buy = min(first_buy, prices[i])
            first_profit = max(first_profit, prices[i] - first_buy)
            second_buy = min(second_buy, prices[i] - first_profit)
            second_profit = max(second_profit, prices[i] - second_buy)
        return second_profit
prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices))
