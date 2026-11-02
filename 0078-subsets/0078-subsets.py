class Solution(object):
    def subsets(self, nums):
        res = []
        temp = []

        def solve(idx):
            if idx == len(nums):
                res.append(temp[:])
                return

            temp.append(nums[idx])
            solve(idx+1)

            temp.pop()
            solve(idx+1)
        
        solve(0)
        return res