class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        myset = [0 for i in range(k+1)]
        res = 0
        j = len(nums)-1
        
        while sum(myset) != k and j >=0:
            if nums[j] >= 1 and nums[j] <= k:
                myset[nums[j]] = 1
                j -= 1
            else:
                j -= 1
            res += 1
        return res
        
