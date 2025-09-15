#
# @lc app=leetcode id=642 lang=python3
#
# [642] Design Search Autocomplete System
#

# @lc code=start
class AutocompleteSystem:

    def __init__(self, sentences: list[str], times: list[int]):
        from collections import defaultdict

        self.trie = {}
        self.counts = defaultdict(int)
        self.current_input = ""

        for sentence, time in zip(sentences, times):
            self.add_sentence(sentence, time)

    def add_sentence(self, sentence: str, time: int):
        node = self.trie
        for char in sentence:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = node.get('#', 0) + time
        self.counts[sentence] += time

    def search(self, prefix: str) -> list[str]:
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]

        results = []

        def dfs(current_node, current_sentence):
            if '#' in current_node:
                results.append((current_sentence, current_node['#']))
            for char, next_node in current_node.items():
                if char != '#':
                    dfs(next_node, current_sentence + char)

        dfs(node, prefix)
        results.sort(key=lambda x: (-x[1], x[0]))
        

    def input(self, c: str) -> list[str]:
        if c == '#':
            self.add_sentence(self.current_input, 1)
            self.current_input = ""
            return []

        self.current_input += c
        return self.search(self.current_input)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
# @lc code=end

