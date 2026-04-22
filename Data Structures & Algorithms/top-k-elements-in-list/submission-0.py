class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each element
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets where bucket[i] contains elements with frequency i
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Collect k most frequent elements from highest frequency buckets
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]

        return result