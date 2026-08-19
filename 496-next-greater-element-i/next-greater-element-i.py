class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[-1]*(len(nums1))
        for i in range(len(nums1)):
            ind=nums2.index(nums1[i])
            for j in range(ind+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    arr[i]=nums2[j]
                    break 
                
        return arr