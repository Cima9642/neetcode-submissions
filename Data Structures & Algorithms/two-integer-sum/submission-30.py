class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # initialize hash map

        for i, n in enumerate(nums): # loop through nums, getting both the index (i) and value (n)
            diff = target - n # find the value missing to equal target
            if diff in seen: # check if the missing piece has been seen before
                return [seen[diff],i] # return both indices
            seen[n] = i # save this value and its index in the map for future lookups
