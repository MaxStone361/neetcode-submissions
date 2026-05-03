class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1
        for ch in t:
            cnt[ch] -= 1

        for c in cnt.values():
            if c != 0:
                return False
        
        return True


        