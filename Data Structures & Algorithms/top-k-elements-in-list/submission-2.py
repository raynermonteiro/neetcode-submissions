class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = Counter(nums)
        sorted_keys = sorted(freqMap, key=freqMap.get, reverse=True)
        
        return sorted_keys[:k]
        