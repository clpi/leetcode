#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
phone = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
# Time complexity: O(4^n * n) where n is the length of digits
# Space complexity: O(n) where n is the length of digits
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        combos = []
        def backtrack(idx: int, path: list[str]):
            if len(path) == len(digits):
                combos.append("".join(path))
                return
            possible = phone[digits[idx]]
            for c in possible:
                path.append(c)
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return combos

            

        
# @lc code=end

