#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        from collections import defaultdict
        if not points:
            return 0
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        max_points = 1
        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    dx = points[j][0] - points[i][0]
                    dy = points[j][1] - points[i][1]
                    if dx == 0:
                        slope = 'inf'
                    elif dy == 0:
                        slope = 0
                    else:
                        g = gcd(dx, dy)
                        slope = (dy // g, dx // g)
                    slopes[slope] += 1
            max_points = max(max_points, max(slopes.values(), default=0) + 1)
        return max_points
                             
        
# @lc code=end

