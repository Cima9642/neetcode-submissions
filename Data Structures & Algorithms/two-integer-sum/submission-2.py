class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,n in enumerate(nums):
            value = target - n
            if value in hash:
                return[hash[value],i]
            hash[n] = i
        