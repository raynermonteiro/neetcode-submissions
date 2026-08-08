from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Standard binary search boundary
        while left < right:
            mid = (left + right) // 2 
            # could use mid = left + (right - left) // 2  Safe calculation prevents integer overflow
            print(left, right, mid)
            
            # If mid element is greater than the rightmost element, 
            # the minimum element must be on the right side of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, mid could be the minimum, or it is to the left.
                right = mid
                
        return nums[left]
