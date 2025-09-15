#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.')))
        
        # Normalize lengths by appending zeros
        max_length = max(len(v1_parts), len(v2_parts))
        v1_parts += [0] * (max_length - len(v1_parts))
        v2_parts += [0] * (max_length - len(v2_parts))
        
        for i in range(max_length):
            if v1_parts[i] < v2_parts[i]:
                return -1
            elif v1_parts[i] > v2_parts[i]:
                return 1
        
        return 0
        
# @lc code=end

