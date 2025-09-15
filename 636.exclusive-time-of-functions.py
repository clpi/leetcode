#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack = []
        result = [0] * n
        prev_time = 0
        
        for log in logs:
            id, status, time = log.split(':')
            id, time = int(id), int(time)
            
            if status == 'start':
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(id)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result

