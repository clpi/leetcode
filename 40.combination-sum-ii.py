#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path)
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])

        result = []
        candidates.sort()
        backtrack(0, [], target)
        return result

# @lc code=end

