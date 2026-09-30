class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        new=nums[::-1]
        s=new[:k][::-1]
        s2=nums[:n-k]
        nums[:]=s+s2
        return nums










