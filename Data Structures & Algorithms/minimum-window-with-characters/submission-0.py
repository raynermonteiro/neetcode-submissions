class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        for c in t:
            tDict[c] = tDict.get(c, 0) + 1
        
        left, right = 0, 0
        #Assume min window is the entire string.
        min_w_len = len(s) + 1
        #Result array to store left and right index
        res = [-1, -1]
        # No. of characters we need in the window from t
        need_chars = len(t)

        while right < len(s):
            #check if the current character is in t
            if s[right] in tDict:
                 #if we have s[right] required in t, reduce need
                if tDict.get(s[right]) > 0:
                    need_chars = need_chars - 1
                #Decress the count of that char in Dict
                tDict[s[right]] = tDict.get(s[right]) - 1
            
            #check if we have all chars, if yes then reduce window from left and see if its still valid
            while need_chars == 0:
                #check if current window is smaller
                if (right - left + 1) < min_w_len: 
                    min_w_len = (right - left + 1) 
                    res = [left, right]

                if s[left] in tDict:
                    tDict[s[left]] = tDict.get(s[left]) + 1
                    # Still, update the counter only if the current char is "critical"
                    if tDict[s[left]] > 0:
                        need_chars += 1
                left +=1
            
            right +=1
        
        if min_w_len == len(s) + 1:
            return ""
        else:
            return s[res[0]:res[1]+1]


        