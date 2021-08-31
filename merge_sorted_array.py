 """
 You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively
 Do not return anything, modify nums1 in-place instead.
        """

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
       
        l=len(nums1)
        t=l-m
        while(t>0):
            nums1.pop()
            t=t-1
        nums1.extend(nums2)
        nums1.sort()