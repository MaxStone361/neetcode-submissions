class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mp = defaultdict(int)
        # 创建空的哈希表 mp = {}, 且具有访问不存在键时默认值为 0”的功能
        for ch in s:
            mp[ch] += 1
        # 当for访问一个不存在元素，如"a"时，会创建 mp = {"a": 1}
        for ch in t:
            mp[ch] -= 1
        # 如果在t中也有"a"，则 mp = {"a": 0}

        for c in mp.values():
            if c != 0:
                return False
        return True


        