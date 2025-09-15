#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.is_end = False
        self.children = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '#' in node
            
            char = word[i]
            if char == '.':
                for child in node:
                    if child != '#':
                        if dfs(node[child], i + 1):
                            return True
            else:
                if char in node and dfs(node[char], i + 1):
                    return True
            
            return False
        
        return dfs(self.trie, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

