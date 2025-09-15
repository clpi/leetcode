#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#

# @lc code=start
class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.word_indices = {}
        for index, word in enumerate(wordsDict):
            if word not in self.word_indices:
                self.word_indices[word] = []
            self.word_indices[word].append(index)
        

    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.word_indices.get(word1, [])
        indices2 = self.word_indices.get(word2, [])
        
        if not indices1 or not indices2:
            return -1
        
        min_distance = int(1e9)
        i, j = 0, 0
        
        while i < len(indices1) and j < len(indices2):
            min_distance = min(min_distance, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1

        return min_distance if min_distance != int(1e9) else -1



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
# @lc code=end

