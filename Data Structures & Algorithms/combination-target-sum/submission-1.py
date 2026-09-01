from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort candidates to enable early pruning of the search tree
        nums.sort()
        
        # dfs tracks:
        # i: current index in nums to avoid duplicate combinations
        # cur: current combination list
        # total: running sum of elements in cur
        def dfs(i, cur, total):
            # Base case: valid combination found
            if total == target:
                res.append(cur.copy())  # Append a shallow copy to prevent mutation
                return
            
            # Explore remaining elements starting from index i
            for j in range(i, len(nums)):
                # Pruning: since nums is sorted, if adding nums[j] exceeds target,
                # all subsequent larger elements will also exceed target
                if total + nums[j] > target:
                    return
                
                # Backtracking: choose the current candidate
                cur.append(nums[j])
                # Recurse: allow reusing the same element by passing index j
                dfs(j, cur, total + nums[j])
                # Backtracking: unchoose the candidate
                cur.pop()
        
        # Start depth-first search from index 0, with empty path and 0 sum
        dfs(0, [], 0)
        return res
