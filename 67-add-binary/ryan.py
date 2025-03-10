# Runtime: 7ms (34.82%), Memory: 12.32MB (85.68%)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a) - 1
        n = len(b) - 1
        carry = 0
        result = []

        while m >= 0 or n >= 0 or carry:
            total = carry

            if m >= 0:
                total += int(a[m])
                m -= 1
            
            if n >= 0:
                total += int(b[n])
                n -= 1
            
            result.append(str(total % 2))
            carry = total // 2
        
        return "".join(result[::-1])
