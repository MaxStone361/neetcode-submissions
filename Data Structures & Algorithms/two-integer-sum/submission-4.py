class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, n in enumerate(nums):
            j = target - n
            if j in mp:
                return[mp[j], i]
            mp[n] = i
                    
        
