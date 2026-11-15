#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        existing_sum = max(candies)
        for i in range(len(candies)):
            curr_sum = candies[i] + extraCandies
            if curr_sum >= existing_sum:
                candies[i] = True
            else:
                candies[i] = False
        return candies
        
# @lc code=end

