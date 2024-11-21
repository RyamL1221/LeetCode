# Runtime: 3ms(64.75%), Memory: 11.70MB (58.29%)
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:  
            return 0

        sign = 1
        if s[0] == '-':  
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        number = ""
        for char in s:
            if char.isdigit():
                number += char
            else:
                break

        if not number:
            return 0

        result = sign * int(number)

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result

