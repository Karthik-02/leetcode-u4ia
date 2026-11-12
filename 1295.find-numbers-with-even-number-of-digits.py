#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        # easy sol - 1 but uses extra space for string conversion
        # digit_count=0
        # for i in nums:
        #     if len(str(i)) % 2 == 0:
        #         digit_count += 1
        # return digit_count
        digit_count = 0
        for i in nums:
            count = 0
            while (i > 0):
                digit = i % 10
                count += 1
                i = i // 10
            if count % 2 == 0:
                digit_count += 1
        return digit_count
                
            
# @lc code=end

