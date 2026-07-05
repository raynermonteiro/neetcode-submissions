class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        rtrnList = []
        for i, num in enumerate(nums):
            diffSum = target - num
            if num in numDict:
                rtrnList.append(numDict[num])
                rtrnList.append(i)
                print(rtrnList)
                break;
            else:
                numDict[diffSum] = i

        print(numDict)
        return rtrnList
            