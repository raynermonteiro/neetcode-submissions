class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = defaultdict(list)
        
        for string in strs:
            sortedS = ''.join(sorted(string))
            resDict[sortedS].append(string)
        
        return list(resDict.values())