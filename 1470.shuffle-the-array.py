#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
       res_arr = []
       for i in range(n):
        res_arr.append(nums[i])
        res_arr.append(nums[i+n])
       return res_arr
# @lc code=end

