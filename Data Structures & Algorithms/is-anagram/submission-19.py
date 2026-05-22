class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if length don't match then makes no sense to check
            return False
        
        countS, countT = {},{} # initialize hashmaps

        for i in range(len(s)): # iterate through the range of length of the array
            countS[s[i]] = 1 + countS.get(s[i], 0) # get value in dictionary , syntax dictionary.get(keyname, value)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT 
