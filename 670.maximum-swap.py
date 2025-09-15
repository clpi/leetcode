#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last_index = {int(digit): i for i, digit in enumerate(num_str)}

        for i, digit in enumerate(num_str):
            for d in range(9, int(digit), -1):
                if last_index.get(d, -1) > i:
                    num_str[i], num_str[last_index[d]] = num_str[last_index[d]], num_str[i]
                    return int(''.join(num_str))

        return num
        
# @lc code=end

