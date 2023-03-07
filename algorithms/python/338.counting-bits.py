#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(n+1):
            res[i] = bin(i).count('1')
        return res
        
# @lc code=end

