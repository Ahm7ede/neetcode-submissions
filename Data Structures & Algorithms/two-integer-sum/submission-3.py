class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        li=[]
        for i in range(len(nums)):
            freq.update({nums[i]:i})
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in freq and i!=freq[diff]:
                li.extend([i,freq[diff]])
                return li
        return li 

