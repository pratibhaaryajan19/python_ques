

"""

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums
"""

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		if nums==[]:
			return -1
		if target==nums[0]:
			return 0
		elif target >nums[0]:
			for i in range(0, len(nums)):
				if nums[i]>target:
					return -1
				if nums[i]==target:
					return i
			return -1
		elif target < nums[0]:
			for i in range(len(nums)-1,-1,-1):
				if nums[i]<target:
					return -1
				if nums[i]==target:
					return i
			return -1