class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # For Odd length Strings
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res = res + 1
                left = left - 1
                right = right + 1
            
            # For even length Strings
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res = res + 1
                left = left - 1
                right = right + 1
        
        return res


        