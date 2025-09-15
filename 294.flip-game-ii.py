#
# @lc app=leetcode id=294 lang=python3
#
# [294] Flip Game II
#

# @lc code=start
class Solution:
    def canWin(self, currentState: str) -> bool:
        def can_win(state):
            for i in range(len(state) - 1):
                if state[i] == '+' and state[i + 1] == '+':
                    new_state = state[:i] + '--' + state[i + 2:]
                    if not can_win(new_state):
                        return True
            return False
        
        return can_win(currentState)
        
# @lc code=end

