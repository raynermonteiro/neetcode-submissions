class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxAmt = 0
        while l < r:
            diff = r-l
            maxNum = min(heights[l],heights[r])
            maxAmt = max(maxAmt, maxNum*diff)
            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r-1
        
        return maxAmt

        