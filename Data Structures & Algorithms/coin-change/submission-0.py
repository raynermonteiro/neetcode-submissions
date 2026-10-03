from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the DP array with infinity for all amounts from 0 to amount.
        # dp[i] will store the minimum number of coins needed to make up amount i.
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins are needed to make up an amount of 0.
        dp[0] = 0 

        # Iterate through all sub-amounts from 1 up to the target amount.
        for i in range(1, amount + 1):
            # Try every available coin denomination.
            for coin in coins:
                # Check if the coin is smaller than or equal to the current sub-amount.
                if i - coin >= 0:
                    # Update dp[i] by taking the minimum of its current value
                    # and the coins needed for the remainder (i - coin) plus 1 (the current coin).
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        
        # If dp[amount] is still infinity, it means the target amount cannot be reached.
        # Otherwise, return the minimum coins calculated for the target amount.
        return dp[amount] if dp[amount] != float('inf') else -1
