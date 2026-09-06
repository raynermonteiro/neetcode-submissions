class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}  # Use a standard dict
        res = 0

        for num in nums:
            if num not in mp:  
                # .get(key, 0) returns 0 if missing, without inserting it
                left = mp.get(num - 1, 0)
                right = mp.get(num + 1, 0)
                
                current_sum = left + right + 1
                mp[num] = current_sum
                
                # Update the boundaries of the sequence
                mp[num - left] = current_sum
                mp[num + right] = current_sum
                
                res = max(res, current_sum)
        return res