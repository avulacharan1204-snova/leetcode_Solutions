class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[k]=nums[i]
                k+=1
        
        return k


# k = position where the next kept element goes (also the count of kept elements)
# i scans the array from start to end
# if nums[i] is not val, copy it to nums[k] and move k forward
# if nums[i] is val, skip it (do nothing), so it gets overwritten later
# return k, the first k slots hold the answer