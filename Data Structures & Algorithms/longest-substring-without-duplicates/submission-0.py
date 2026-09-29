class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        hasht=set()
        maxl=0
        for r in range(len(s)):
            while s[r] in hasht:
                hasht.remove(s[l])
                l+=1
            else:
                hasht.add(s[r]) 
                maxl=max(maxl,r-l+1)
        return maxl

