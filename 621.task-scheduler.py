#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        from collections import Counter
        
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)
        
        # Calculate the number of intervals needed
        intervals = (max_count - 1) * (n + 1) + max_count_tasks

        return max(intervals, len(tasks)) 
# @lc code=end

