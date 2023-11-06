class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Two pointers. Another is inside the loop.
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s

sol = Solution()
print(sol.reverseStr("abcdefg", 2))
# s = "abcdefg"
# a = s[:]
# print(id(s)==id(a))
# print(s==a)
# # s_ = s
# s_[0] = 'b'
# print(a)