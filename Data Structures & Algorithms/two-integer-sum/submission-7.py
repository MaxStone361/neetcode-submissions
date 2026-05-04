class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, j in enumerate(nums):
            # nums = [3, 4, 5, 6]
            # list(enumerate(nums)=[(0,3),(1,4),(2,5),(3,6)]
            diff = target - j

            if diff in mp:
                return [mp[diff], i]
                # 一旦找到匹配项立刻结束并返回两个索引
                # 假设在第二轮循环中,targe = 7, j = 4
                # 那么 diff = 3 是存在于dict中的,mp = {3:0}
                # 因此 return(mp[3], 1) 即(0,1)

            mp[j] = i
