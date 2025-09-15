#
# @lc app=leetcode id=293 lang=python3
#
# [293] Flip Game
#

# @lc code=start
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []
        n = len(currentState)

        for i in range(n - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                new_state = currentState[:i] + '--' + currentState[i + 2:]
                result.append(new_state)

        return result
        
# @lc code=end

