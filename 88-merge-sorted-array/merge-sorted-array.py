class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        array1, array2 = m-1, n-1
        limiter = m + n - 1

        while array1 >=0 and array2 >=0:
            if nums1[array1] > nums2[array2]:
                nums1[limiter] = nums1[array1]

                array1 -= 1
            else:
                nums1[limiter] = nums2[array2]
                array2 -= 1
            limiter -=1

        nums1[:array2 + 1] = nums2[:array2 + 1]          