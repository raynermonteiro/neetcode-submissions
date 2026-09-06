class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = Counter(s)
        mapT = Counter(t)
        return mapS == mapT
       
        