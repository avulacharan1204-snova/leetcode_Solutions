class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        Map = {}

        for i,num in enumerate(nums):
            complement = target-num
            if complement in Map:
                return [Map[complement],i]
            
            Map[num] = i
