class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        # defaultdict(type)中的类型指创建的dict中值的类型
        # 即在这个练习中，dict的值是一个列表，如：["act" : ["act","cat"]]

        for st in strs:
            key = " ".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())
