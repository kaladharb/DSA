class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        freq={0:1}
        prifix_sum=0
        for i in nums:
            prifix_sum+=i

            if (prifix_sum-k) in freq:
                count+=freq[prifix_sum-k]

            freq[prifix_sum]=freq.get(prifix_sum,0)+1
        return count

      