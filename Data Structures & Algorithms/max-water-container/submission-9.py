class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # If the current smallest number is positive, 3 elements can never sum to 0
            if num > 0:
                break

            # Skip duplicates for the first element
            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                diff = nums[left] + nums[right] + num
                
                if diff == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Safe duplicate skipping (bound check comes first)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif diff > 0:
                    right -= 1  # Sum is too big, make it smaller
                else:
                    left += 1   # Sum is too small, make it bigger
                    
        return res
