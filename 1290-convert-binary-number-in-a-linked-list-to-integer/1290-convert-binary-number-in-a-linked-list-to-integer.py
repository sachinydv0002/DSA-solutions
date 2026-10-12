class Solution(object):
    def getDecimalValue(self, head):
        ans = 0
        curr = head
        while curr:
            ans = ans * 2 + curr.val
            curr = curr.next
        return ans