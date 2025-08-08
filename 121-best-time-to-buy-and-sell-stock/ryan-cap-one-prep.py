# Runtime: O(n), 91ms (52.45%); Memory: O(1), 27.06MB (8.23%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit
