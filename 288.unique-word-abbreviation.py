#
# @lc app=leetcode id=288 lang=python3
#
# [288] Unique Word Abbreviation
#

# @lc code=start
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr_map = {}
        for word in dictionary:
            abbr = self._get_abbreviation(word)
            if abbr in self.abbr_map:
                self.abbr_map[abbr].add(word)
            else:
                self.abbr_map[abbr] = {word}
        
    def _get_abbreviation(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        abbr = self._get_abbreviation(word)
        if abbr not in self.abbr_map:
            return True
        return len(self.abbr_map[abbr]) == 1 and word in self.abbr_map[abbr]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
# @lc code=end

