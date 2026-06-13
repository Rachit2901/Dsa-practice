class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)/2
        d1={}
        for el in nums:
            if el in d1:
                d1[el]+=1
            else:
                d1[el]=1
        for key,val in d1.items():
            if(val>n):
              return key
              break


        