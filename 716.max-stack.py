#
# @lc app=leetcode id=716 lang=python3
#
# [716] Max Stack
#

# @lc code=start
class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])
        

    def pop(self) -> int:
        if not self.stack:
            return None
        self.max_stack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]
        

    def peekMax(self) -> int:
        if not self.max_stack:
            return None
        return self.max_stack[-1]
        

    def popMax(self) -> int:
        if not self.max_stack:
            return None
        max_value = self.max_stack.pop()
        temp_stack = []
        
        while self.stack and self.stack[-1] != max_value:
            temp_stack.append(self.stack.pop())
        
        if self.stack:
            self.stack.pop()

        while temp_stack:
            self.push(temp_stack.pop())
        return max_value
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
# @lc code=end

