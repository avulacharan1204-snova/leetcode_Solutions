class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0 
        right = 1

        while right<len(nums):
            if nums[left]!=nums[right]:
                left+=1
                nums[left]=nums[right]
            right+=1
        
        return left+1

# left marks the last unique value placed (starts at index 0)
# right scans the array one step at a time
# if nums[right] differs from nums[left], it is a new unique value:
#     move left forward and copy nums[right] into nums[left]
# return left + 1, the count of unique elements

        