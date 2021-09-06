"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
"""leetcode question"""
class Solution:
    def canJump(self, n: List[int]) -> bool:
    	m = 0
    	for i in range(len(n)-1):
    		m = max(m, n[i] + i)
    		if n[i] != 0: continue
    		if m <= i: return False
    	return True
