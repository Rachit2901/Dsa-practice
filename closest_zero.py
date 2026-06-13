# LeetCode 2239 - Find Closest Number to Zero
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cl=(nums[0])       
        for el in nums:
            if(abs(el)<abs(cl)):
                cl=el
            elif(abs(el)==abs(cl)):
                cl=max(el,cl)
        return cl


        


       
                    
        

        