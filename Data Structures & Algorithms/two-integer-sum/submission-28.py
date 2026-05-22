class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # initialize hash map

        for i, n in enumerate(nums): # loop through i and keep track of the pointer as well as return the indeces
            diff = target - n # finds the value missing to equal to target
            if diff in seen:
                return [seen[diff],i]
            seen[n] = i         