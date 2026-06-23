class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1
        def pc(i,f):
            
            while(i<=f):
                if(s[i]==s[f]):
                    i+=1
                    f-=1
                else:
                    return False
                    
            return True

        while(left<=right):
            if(s[left]==s[right]):
                left+=1
                right-=1
                

            else:
                return (pc(left+1,right) or pc(left,right-1))
        return True
            
            