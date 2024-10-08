class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = prices[0]
        min_price = prices[0]
        profit = 0

        for price in prices:
            if price > max_price:
                max_price = price
                curr = max_price - min_price
                profit = max(profit, curr)
            elif price < min_price:
                max_price = price
                min_price = price
        
        return profit