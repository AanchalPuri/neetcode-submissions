class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for i, num in enumerate(nums):
            other_val = target - num
            
            if other_val in found:
                return [found[other_val], i]
        
            found[num] = i

        return []

    