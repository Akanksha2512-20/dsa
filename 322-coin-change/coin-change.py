class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Fill the dp array for each amount from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # Update dp[i] with the minimum coins required
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is inf, it means we cannot form the amount with given coins
        return dp[amount] if dp[amount] != float('inf') else -1