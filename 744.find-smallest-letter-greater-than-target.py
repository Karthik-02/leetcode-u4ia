#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        start, end = 0, len(letters)-1
        while(start<=end):
            mid = int((start + end)/2)
            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return letters[start % len(letters)]
# @lc code=end

