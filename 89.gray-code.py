#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# where n is the number of bits in the binary representation:
# Time complexity: O(2^n): the max depth of the recursive function stack
#     is n. At every function call we iterate over the list result and
#     at each iteration we add a new number to the result list. At n=1
#     we iterate over the list [0] of size 2^0=1, next at n=2 we iterate
#     over the list [0, 1] of size 2^1=2. Likewise at n=3.
# Space complexity: O(n) We start from n and continue our recursive 
#     function call until our base condition n=0 is reached.

# @lc code=start
class Solution:
    def grayCodeHelper(self, res: list[int], n: int):
        if n == 0:
            res.append(0)
            return
        self.grayCodeHelper(res, n - 1)
        curr_seq_len = len(res)
        mask = 1 << (n - 1)
        for i in range(curr_seq_len - 1, -1, -1):
            res.append(res[i] | mask)
        return

    def grayCode(self, n: int) -> list[int]:
        result = []
        self.grayCodeHelper(result, n)
        return result
        
# @lc code=end

