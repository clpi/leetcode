#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_key(s):
            if len(s) == 1:
                return (0,)
            return tuple((ord(s[i]) - ord(s[i - 1])) % 26 for i in range(1, len(s)))

        groups = defaultdict(list)
        for s in strings:
            key = get_key(s)
            groups[key].append(s)

        return list(groups.values())

# @lc code=end

