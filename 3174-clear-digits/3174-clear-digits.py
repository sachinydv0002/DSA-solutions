class Solution(object):
    def clearDigits(self, s):
        ans = []
        for ch in s:
            if ch.isdigit():
                ans.pop()
            else: ans.append(ch)
        return "".join(ans)