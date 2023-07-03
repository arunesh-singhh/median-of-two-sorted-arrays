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

#approach-3
class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        a, b = num1, num2
        total = len(num1) + len(num2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        l, r = 0, len(a) - 1
        while True:
            px = (l + r) // 2   # a
            py = half - px - 2   # b

            aleft = a[px] if px >= 0 else float("-inf")
            aright = a[px + 1] if (px + 1) < len(a) else float("inf")
            bleft = b[py] if py >= 0 else float("-inf")
            bright = b[py + 1] if (py + 1) < len(b) else float("inf")

            if aleft <= bright and bleft <= aright:    # check partition is correct
                if total % 2:    # odd
                    return min(aright, bright)
                else:      # even
                    return(max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = px - 1
            else:
                l = px + 1
