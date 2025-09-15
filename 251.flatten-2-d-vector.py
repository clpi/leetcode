#
# @lc app=leetcode id=251 lang=python3
#
# [251] Flatten 2D Vector
#

# @lc code=start
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = 0
        self.rows = len(vec)
        self.cols = [len(row) for row in vec]
        

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration("No more elements in the vector")
        
        value = self.vec[self.row][self.col]
        self.col += 1
        
        if self.col == self.cols[self.row]:
            self.row += 1
            self.col = 0
            
        return value
        

    def hasNext(self) -> bool:
        while self.row < self.rows and self.col >= self.cols[self.row]:
            self.row += 1
            self.col = 0
            
        return self.row < self.rows and self.col < self.cols[self.row]
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

