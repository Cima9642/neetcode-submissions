class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            number_count[num] = 1 + number_count.get(num, 0)
        
        for num, frequency in number_count.items():
            buckets[frequency].append(num)
        
        top_k_numbers = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k_numbers.append(num)
                if len(top_k_numbers) == k:
                    return top_k_numbers
                    