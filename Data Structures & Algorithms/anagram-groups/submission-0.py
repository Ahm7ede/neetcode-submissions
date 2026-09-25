class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for i in strs:
            temp="".join(sorted(i))
            if temp not in freq:
                freq.update({temp:[i]})
            else:
                freq[temp].append(i)
        return list(freq.values())
