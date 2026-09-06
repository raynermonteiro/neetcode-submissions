class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = {}
        for string in strs:
            countArr = [0] * 26
            for char in string:
                countArr[ord(char) - ord('a')] += 1
            currList = countMap.get(tuple(countArr), [])
            currList.append(string)
            countMap[tuple(countArr)] = currList
        
        return list(countMap.values())
        