class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = {}

        differential = enumerate

        for i, j in differential(nums):
            difference = target - j
            if difference in hashset:
                return [hashset[difference], i]
            hashset[j] = i
        return []
