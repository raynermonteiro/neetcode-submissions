class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        for i in range(0, n):
            if i == 0 or i == 1:
                dp[i] = nums[i]
            elif i == 2:
                dp[i] = nums[i] + dp[i-2]
            else:
                dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        print(dp)
        return max(dp[n-1], dp[n-2])



        