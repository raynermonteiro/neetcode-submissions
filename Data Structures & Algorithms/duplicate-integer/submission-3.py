class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uqSet = set(nums)
        print(uqSet)
        if len(uqSet) == len(nums):
            return False
        return True
        