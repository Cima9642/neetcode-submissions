class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #hasmap initiated

        for s in strs: #loops through strs and stores it in s
            count = [0] * 26 # gives us 26 0s to store the count
            for c in s: 
                count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(s)
        return list(res.values())
        