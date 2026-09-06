class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i,num in enumerate(nums):
            numMap[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in numMap and numMap[diff] != i:
                return [i, numMap[diff]]
        
            
        