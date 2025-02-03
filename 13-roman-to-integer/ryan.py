# Runtime: 17ms(19.78%), Memory: 12.38MB(69.98%)
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        val = [
            1000, 900, 500, 400, 100, 90, 
            50, 40, 10, 9, 5, 4, 1
        ]
        symbols = [
            "M", "CM", "D", "CD", "C", "XC", 
            "L", "XL", "X", "IX", "V", "IV", "I"
        ]
        for i in range(len(symbols)):
            while s.startswith(symbols[i]):
                result += val[i]
                s = s[len(symbols[i]):]
        return result
                    
