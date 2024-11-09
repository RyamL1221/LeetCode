# Runtime: 17ms (48.86%), Memory: 11.70MB (29.13%)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x > 0):
            x = str(x)
            x = x[::-1]
            x = int(x)
        elif(x < 0):
            x = str(x)
            x = x[1:len(x)]
            x = x[::-1]
            x = int(x)
            x *= - 1
        else:
            return 0
        if x < pow(-2, 31) or x > pow(2, 31) - 1:
            return 0
        return x
        
