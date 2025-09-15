#
# @lc app=leetcode id=254 lang=python3
#
# [254] Factor Combinations
#

# @lc code=start
class Solution:
    def getFactors(self, n: int) -> list[list[int]]:
        def backtrack(start, path):
            if n == 1:
                if len(path) > 1:
                    result.append(path[:])
                return
            
            for i in range(start, int(n**0.5) + 1):
                if n % i == 0:
                    path.append(i)
                    backtrack(i, path)
                    path.pop()
                    n //= i
                    path.append(n)
                    backtrack(i, path)
                    path.pop()
                    n *= i

        result = []
        backtrack(2, [])
        return result
        
# @lc code=end

