class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1
        for ch in t:
            mp[ch] -= 1

        for c in mp.values():
            if c != 0:
                return False
        return True


        