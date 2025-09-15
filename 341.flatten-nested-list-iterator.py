#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.stack = []
        self._push_left(nestedList)

    # Push all elements of the nested list onto the stack
    # in reverse order so that we can pop them in the correct order
    # when calling next().
    def _push_left(self, nestedList: list[NestedInteger]):
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # If the top is a nested list, pop it and push its elements onto the stack
            self.stack.pop()
            self._push_left(top.getList())
        return False

    def next(self) -> int:
        if not self.hasNext():
            return -1
        return self.stack.pop().getInteger()


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

