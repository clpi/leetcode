#
# @lc app=leetcode id=527 lang=python3
#
# [527] Word Abbreviation
#

# @lc code=start
from collections import defaultdict
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbreviate(word, k):
            if len(word) <= k + 2:
                return word
            return word[:k] + str(len(word) - k - 1) + word[-1]

        n = len(words)
        abbrs = [abbreviate(word, 1) for word in words]
        count = defaultdict(int)
        
        for abbr in abbrs:
            count[abbr] += 1
        
        result = []
        for i in range(n):
            if count[abbrs[i]] > 1:
                k = 1
                while True:
                    new_abbr = abbreviate(words[i], k)
                    if count[new_abbr] == 1:
                        result.append(new_abbr)
                        break
                    k += 1
            else:
                result.append(abbrs[i])
        
        return result
        
# @lc code=end

