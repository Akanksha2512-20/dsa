class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        j = 0
        for i in range(1,len(prices)):
            if prices[i]> prices[j]:
               maxprofit = max(maxprofit,prices[i]-prices[j])
            else:
                j = i
        return maxprofit       
