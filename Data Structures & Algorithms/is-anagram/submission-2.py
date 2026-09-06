class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If Length is not same the the wont have same chars
        if len(s) != len(t):
            return False
        
        #Create array of 26 len with 0 as counter for each char
        countArr = [0] * 26
        for i in range(len(s)):
            #Increment count for every char in S
            countArr[ord(s[i]) - ord('a')] += 1
            #Decrement count for every char in t
            countArr[ord(t[i]) - ord('a')] -= 1
        
        for cnt in countArr:
            #if we find a non zero count return false
            if cnt != 0:
                return False
        
        return True
        