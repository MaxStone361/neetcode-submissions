class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        res = 0
        left = 0
        maxf = 0

        for right in range(len(s)):
            mp[s[right]] = 1 + mp.get(s[right], 0)
            maxf = max(maxf, mp[s[right]])

            while (right-left+1) - maxf > k:
                mp[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)

        return res
