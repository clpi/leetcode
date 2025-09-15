#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#

# @lc code=start
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0

        m, n = len(image), len(image[0])
        
        # Find the boundaries of the rectangle
        left, right = y, y
        top, bottom = x, x

        # Search for the left boundary
        while left > 0 and any(image[i][left - 1] == '1' for i in range(m)):
            left -= 1
        
        # Search for the right boundary
        while right < n - 1 and any(image[i][right + 1] == '1' for i in range(m)):
            right += 1
        
        # Search for the top boundary
        while top > 0 and any(image[top - 1][j] == '1' for j in range(left, right + 1)):
            top -= 1
        
        # Search for the bottom boundary
        while bottom < m - 1 and any(image[bottom + 1][j] == '1' for j in range(left, right + 1)):
            bottom += 1

        return (right - left + 1) * (bottom - top + 1)
        
# @lc code=end

