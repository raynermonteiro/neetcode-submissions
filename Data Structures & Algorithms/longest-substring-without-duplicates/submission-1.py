class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        uniqueSet = set()
        maxLen = 0
        while right < len(s):
            if s[right] not in uniqueSet:
                uniqueSet.add(s[right])
                right = right + 1
                maxLen = max(maxLen , right - left)
            else:
                while s[right] in uniqueSet:
                    uniqueSet.remove(s[left])
                    left = left + 1
        
        return maxLen
            

        