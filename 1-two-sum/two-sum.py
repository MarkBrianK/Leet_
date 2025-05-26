class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}

        for i, num in enumerate(nums):
            number = target - num

            if number in result:
                return [result[number], i]

            result[num] = i

        return []
            
        