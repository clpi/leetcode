#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        count_s1 = Counter(s1)
        count_window = Counter(s2[:len_s1])

        if count_s1 == count_window:
            return True

        for i in range(len_s1, len_s2):
            count_window[s2[i]] += 1
            count_window[s2[i - len_s1]] -= 1

            if count_window[s2[i - len_s1]] == 0:
                del count_window[s2[i - len_s1]]

            if count_s1 == count_window:
                return True

        return False
        
# @lc code=end

