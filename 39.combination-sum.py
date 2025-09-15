#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path)
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                backtrack(i, path + [candidates[i]], remaining - candidates[i])
        
        result = []
        candidates.sort()
        backtrack(0, [], target)
        return result
        
# @lc code=end

