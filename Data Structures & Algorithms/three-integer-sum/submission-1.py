class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            #边界判断，当出现第一个大于0的数时，sum不会再等于0

            if i > 0 and nums[i] == nums[i-1]:
                continue
            #外循环去重：这里i表示索引，即i从第一个元素开始。跳过重复出现的元素，防止出现重复解

            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    #内循环去重：防止第二个数出现重复数字
        return res
