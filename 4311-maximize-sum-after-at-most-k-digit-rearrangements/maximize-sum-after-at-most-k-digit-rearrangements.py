class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:

        arr = []
        for num in nums:
            digits = sorted(str(num), reverse=True)
            new_num = int("".join(digits))
            arr.append((new_num - num, new_num))

        arr.sort(reverse=True)

        total = sum(nums)

        for i in range(min(k, len(arr))):
            total += arr[i][0]

        return total
        