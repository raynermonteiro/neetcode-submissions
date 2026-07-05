class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create frequency List with every index having a list
        freq = [[] for i in range(len(nums)+1)]
        print(freq)
        
        seenDict = defaultdict()
        for num in nums:
            seenDict[num] = 1 + seenDict.get(num, 0)

        print(seenDict)
        for num, count in seenDict.items():
            print(num, count)
            freq[count].append(num)
        
        rtrnList = []
        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                rtrnList.append(num)
                if len(rtrnList) == k:
                    return rtrnList

        return []
        