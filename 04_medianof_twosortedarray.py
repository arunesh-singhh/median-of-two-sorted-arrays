#approach-1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        length = len(nums3)

        half = (len(nums3) + 1) // 2

        if length % 2 == 0:
            return (nums3[half-1] + nums3[half]) / 2
        else:
            return nums3[half-1]