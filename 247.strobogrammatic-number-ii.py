#
# @lc app=leetcode id=247 lang=python3
#
# [247] Strobogrammatic Number II
#

# @lc code=start
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def generate(current, remaining):
            if remaining == 0:
                result.append(current)
                return
            if remaining == 1:
                for digit in ['0', '1', '8']:
                    generate(current + digit, remaining - 1)
                return
            
            for pair in [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]:
                generate(current + pair[0], remaining - 2)
        
        result = []
        generate('', n)
        return result
        
# @lc code=end

