class Solution:
    def isValid(self, s: str) -> bool:
        stk =[]
        close_open = { ")":"(", "]":"[", "}":"{" }

        for c in s:
            if c in close_open:
                if stk and stk[-1] == close_open[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
                
        return True if not stk else False