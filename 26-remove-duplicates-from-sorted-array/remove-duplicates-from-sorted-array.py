class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        slow = 0

        for k in range(1, len(nums)):
            if nums[k] != nums[slow]:
                slow += 1
                nums[slow] = nums[k]
        return slow + 1            
        