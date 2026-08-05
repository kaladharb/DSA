class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new=nums1[:m]+nums2[:n]
        new.sort()
        nums1[:]=new

        return nums1