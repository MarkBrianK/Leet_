class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i, num in enumerate(nums):
            true_num = target - num
            if true_num in result:
                return [result[true_num],i]

            result[num] = i    
            