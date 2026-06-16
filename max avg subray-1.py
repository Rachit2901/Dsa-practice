class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        t=0
        i=0
        window_avg=0
        
       
        while i<=k-1:
            window_avg+=nums[i]
            i+=1
        sliding_avg=window_avg
        n=window_avg      
        for m in range(0,len(nums)-k):
            sliding_avg=sliding_avg-nums[m]+nums[m+k]
            n=max(n,sliding_avg)
        

        return float(n)/k

        