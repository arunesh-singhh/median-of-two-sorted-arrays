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


#approach-2
class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        x = len(num1)
        y = len(num2)

        if x > y:
            return self.findMedianSortedArrays(num2, num1)
        
        low = 0
        high = x

        while low <= high:
            px = (low + high)//2
            py = ((x + y + 1)//2) - px

            maxlx = float("-inf") if px == 0 else num1[px-1]
            minrx = float("-inf") if px == x else num1[px]
            maxly = float("-inf") if py == 0 else num2[py-1]
            minry = float("-inf") if py == y else num2[py]

            if maxlx <= minry and maxly <= minrx:
                if (x + y) % 2 == 0:
                    return(max(maxlx, maxly) + min(minrx, minry)) / 2
                else:
                    return(max(maxlx, maxly))
            elif maxlx > minry:
                high = px - 1
            else:
                low = px + 1
