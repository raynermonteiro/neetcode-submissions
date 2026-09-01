class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, sol, total):
            if target == total:
                res.append(sol.copy())
                return
            for j in range(idx, len(nums)):
                if total + nums[j] > target:
                    return
                sol.append(nums[j])
                dfs(j, sol, total + nums[j])
                sol.pop()
        
        
        dfs(0, [], 0)
        return res
        