#
# @lc app=leetcode id=245 lang=python3
#
# [245] Shortest Word Distance III
#

# @lc code=start
class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        index1, index2 = -1, -1
        min_distance = int(1e9)
        if word1 == word2:
            for i, word in enumerate(wordsDict):
                if word == word1:
                    if index1 != -1:
                        min_distance = min(min_distance, i - index1)
                    index1 = i
        else:
            for i, word in enumerate(wordsDict):
                if word == word1:
                    index1 = i
                elif word == word2:
                    if index1 != -1:
                        min_distance = min(min_distance, i - index1)
                    index2 = i
