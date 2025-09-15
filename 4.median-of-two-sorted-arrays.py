#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        half = total_length // 2
        is_even = total_length % 2 == 0

        def find_kth(k):
            index1, index2 = 0, 0
            while True:
                if index1 == len(nums1):
                    return nums2[index2 + k - 1]
                if index2 == len(nums2):
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                mid_index1 = min(index1 + k // 2 - 1, len(nums1) - 1)
                mid_index2 = min(index2 + k // 2 - 1, len(nums2) - 1)

                if nums1[mid_index1] <= nums2[mid_index2]:
                    k -= (mid_index1 - index1 + 1)
                    index1 = mid_index1 + 1
                else:
                    k -= (mid_index2 - index2 + 1)
                    index2 = mid_index2 + 1

        if is_even:
            return (find_kth(half) + find_kth(half + 1)) / 2
        else:
            return find_kth(half + 1)
        
# @lc code=end

