class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [0]*l
        suffix = [0]*l

        prefix[0] = 1
        for i in range(1,l):
            prefix[i] = nums[i-1] * prefix[i-1]

        print(prefix)

        suffix[l-1] = 1
        for i in range(l-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        print(suffix)

        res = [0] * l
        for i in range(l):
            res[i] = prefix[i] * suffix[i]
        
        return res


        