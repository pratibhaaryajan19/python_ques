""" Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""

 

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=Counter(nums)
        lst=[]
        for ch in res:
            if res[ch]==1:
                lst.append(ch)
        return lst[0]