class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i ,n in enumerate(nums):
            val = target - n
            if val in hash:
                return [hash[val],i]
            hash[n] = i