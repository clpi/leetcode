#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        self.lower_half = []
        self.upper_half = []

        

    def addNum(self, num: int) -> None:
        if not self.lower_half or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)

        # Balance the heaps
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

        if len(self.lower_half) > 1:
            heapq.heappop(self.lower_half)
        

    def findMedian(self) -> float:
        if len(self.lower_half) % 2 == 1:
            return -self.lower_half[0]
        else:
            return (-self.lower_half[0] + -self.lower_half[1]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

