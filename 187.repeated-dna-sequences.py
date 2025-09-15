#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)

        return list(repeated)
        
# @lc code=end

