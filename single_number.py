class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d1={}
        for el in nums:
            if el in d1:
                d1[el]+=1
            else:
                d1[el]=1
        for key,val in d1.items():
            if(val==1):
                return key
                break