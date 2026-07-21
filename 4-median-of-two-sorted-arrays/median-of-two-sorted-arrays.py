class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nlist = nums1+nums2
        nlist.sort()
        l = len(nlist)
        if l%2 == 0:
            nl = l//2
            return (nlist[nl]+nlist[nl-1])/2
        else:
            nl = l//2
            return nlist[nl]