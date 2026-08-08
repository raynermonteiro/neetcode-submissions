class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkDict = { ')':'(', ']': '[', '}':'{'}

        for c in s:
            if c in checkDict:
                if stack and stack.pop() == checkDict[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
 
        