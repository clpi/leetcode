#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        from collections import defaultdict, deque

        graph = defaultdict(set)
        in_degree = defaultdict(int)

        # Initialize in-degree for each character
        for word in words:
            for char in word:
                in_degree[char] = 0

        # Build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_length = min(len(w1), len(w2))
            found_difference = False
            
            for j in range(min_length):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    found_difference = True
                    break
            
            # If w1 is longer than w2 and no difference was found, it's invalid
            if not found_difference and len(w1) > len(w2):
                return ""

        # Topological sort using Kahn's algorithm
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(order) if len(order) == len(in_degree) else ""

# @lc code=end

