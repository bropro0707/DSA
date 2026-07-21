class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        append = res.append
        for i in range(n - 2):
            a = nums[i]
            if a > 0:
                break
            if i and a == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res