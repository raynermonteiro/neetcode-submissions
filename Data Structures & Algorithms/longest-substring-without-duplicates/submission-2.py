class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxLen = 0
        seenSet = set()
        while right < len(s):
            while s[right] in seenSet:
                seenSet.remove(s[left])
                left += 1
            
            seenSet.add(s[right])
            maxLen = max(maxLen, (right - left) + 1)
            right = right + 1
        
        return maxLen