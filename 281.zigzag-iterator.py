#
# @lc app=leetcode id=281 lang=python3
#
# [281] Zigzag Iterator
#

# @lc code=start
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i, self.j = 0, 0
        self.turn = 0
        


    def next(self) -> int:
        if self.turn % 2 == 0:
            if self.i < len(self.v1):
                value = self.v1[self.i]
                self.i += 1
            else:
                value = self.v2[self.j]
                self.j += 1
        else:
            if self.j < len(self.v2):
                value = self.v2[self.j]
                self.j += 1
            else:
                value = self.v1[self.i]
                self.i += 1
        
        self.turn += 1
        return value
        

    def hasNext(self) -> bool:
        return self.i < len(self.v1) or self.j < len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

