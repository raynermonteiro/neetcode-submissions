class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) ## Store nums in set to avoid duplicates
        maxLen = 0

        for num in numSet:
            #Check if this num is begining of the sequence.
            #This can be done by checking if previous num in seq Exists in the set or no
            if (num-1) not in numSet:
                #if it is the begining then set length of subSeq as 1
                length = 1
                #keep checking for next nums in seq in numSet
                while (num+length) in numSet:
                    length += 1
                #store the max Len of subseq
                maxLen = max(maxLen , length)
        

        return maxLen
                

        