class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            # we dont need to check for starting positive integers since we will only encounter +ve as list is sorted.
            if num > 0:
                break

            #skip duplicates
            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                diff = nums[left] + nums[right] + num
                if diff == 0:
                    res.append([num, nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    #Skip duplicate numbers.
                    while nums[left] == nums[left-1] and left < right:
                        left +=1

                elif diff > 0:
                    right = right - 1
                else:
                    left = left + 1
        return res