class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp=set(nums)
        length=0
        longest=0
        for i in temp:
            if i-1 not in temp:
                length=1
                while i+length in temp:
                    length+=1
                longest=max(longest,length)
        return longest

