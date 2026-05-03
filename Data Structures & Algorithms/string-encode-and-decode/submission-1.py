class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + "&" + s
            # st的类型是字符串，len()得到的值是int，注意类型转换
        return st

    def decode(self, s: str) -> List[str]:
      res = []
      i = 0

      while i < len(s):
        j = i
        while s[j] != "&":
            j += 1

        length = int(s[i:j])
        # 这里再次注意类型转换
        word = s[j+1 : j+1+length]
        res.append(word)

        i = j + 1 + length
        
      return res

