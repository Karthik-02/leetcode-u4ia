#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def bound_search_bin(self, nums, target, is_left_most):
        ans = -1
        start, end = 0, len(nums) -1
        while(start<=end):
            mid = int((start+end)/2)
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                ans = mid
                if is_left_most:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = self.bound_search_bin(nums, target, True)
        end = self.bound_search_bin(nums, target, False)
        return [start,end]
# @lc code=end

