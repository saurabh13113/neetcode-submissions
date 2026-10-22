class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mnpr = prices[0]
        for curr in prices:
            if curr < mnpr:
                mnpr = curr
            if curr != mnpr and curr - mnpr > mx:
                mx = curr - mnpr
        return mx