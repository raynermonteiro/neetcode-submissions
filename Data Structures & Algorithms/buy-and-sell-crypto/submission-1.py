class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            bestPrice = min(bestPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - bestPrice)
        
        return maxProfit


        