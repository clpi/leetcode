#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start

# Using a stack to keep track of indices of the height array.
# Complexity:
#    - Time: O(n) where n is the length of the height array
#        - Single iteration of O(n) in which each bar can be touched at most
#          twice (once when added to the stack and once when popped).
#        - Each bar is processed in constant time.
#    - Space: O(n) for the stack in the worst case

class Solution:
    def trap(self, height: list[int]) -> int:
        res, curr, st = 0, 0, []
        while curr < len(height):
            while len(st) != 0 and height[curr] > height[st[-1]]:
                top = st[-1]
                st.pop()
                if len(st) == 0:
                    break
                dist = curr - st[-1] - 1
                h_bounded = (min(height[curr], height[st[-1]]) - height[top])
                res += dist * h_bounded
            st.append(curr)
            curr += 1
        return res


        
# @lc code=end

