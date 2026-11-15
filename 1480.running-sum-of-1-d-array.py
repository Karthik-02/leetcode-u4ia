#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        run_sum = []
        sum_arr = 0
        for i in range(len(nums)):
            sum_arr += nums[i]
            run_sum.append(sum_arr)
        return run_sum
# @lc code=end

