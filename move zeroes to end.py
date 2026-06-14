class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len( nums)-1
        for el in nums:
            if(el!=0):
                nums[i]=el
                i+=1
        for i in range(i,len(nums))  :
            nums[i]=0
            