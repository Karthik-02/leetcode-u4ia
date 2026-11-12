#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            current_wealth = 0
            for j in range(len(accounts[i])):
                current_wealth += accounts[i][j]
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return max_wealth
# @lc code=end

