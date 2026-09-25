class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        output=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        res=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        i=0
        l=list(res.keys())
        while i<k:
            output.append(l[i])
            i+=1
        return output