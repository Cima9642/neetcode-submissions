class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash = set() # initialize hashmap

        for n in nums: # iterate through nums and give value to n
            if n in hash: # check if target is in the hashmap
                return True 
            hash.add(n) # add target to hashmap
        return False