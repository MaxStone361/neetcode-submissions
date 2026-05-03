class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if (num - 1) not in s: 
            # 判断x前有无连续元素，否则x作为序列起点
                length = 1

                while (num + length) in s:
                    length += 1

                longest = max(longest, length)
                # 将先前长度与当前长度比较，取最大值

        return longest