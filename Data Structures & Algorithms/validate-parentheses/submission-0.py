class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        ClosetoOpen = {")":"(", "]":"[", "}": "{" }

        for c in s:
            if c in ClosetoOpen:
                if stk and stk[-1] == ClosetoOpen[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return True if not stk else False
        