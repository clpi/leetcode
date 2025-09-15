#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#

# @lc code=start
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        island_count = 0

        for x, y in positions:
            pos = (x, y)
            if pos not in parent:
                parent[pos] = pos
                rank[pos] = 0
                island_count += 1

                for dx, dy in directions:
                    neighbor = (x + dx, y + dy)
                    if neighbor in parent:
                        if find(pos) != find(neighbor):
                            union(pos, neighbor)
                            island_count -= 1

            result.append(island_count)

        return result
        
# @lc code=end

