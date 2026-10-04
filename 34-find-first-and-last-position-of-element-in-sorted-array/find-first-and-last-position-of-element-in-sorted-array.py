class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find_first():
            l = 0
            h = len(nums) - 1
            ans = -1

            while l <= h:
                mid = (l + h) // 2

                if nums[mid] == target:
                    ans = mid
                    h = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1

            return ans

        def find_last():
            l = 0
            h = len(nums) - 1
            ans = -1

            while l <= h:
                mid = (l + h) // 2

                if nums[mid] == target:
                    ans = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1

            return ans

        return [find_first(), find_last()]