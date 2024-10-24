class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestLength = 0 # length variable
        for i in range(len(s)): # for loop, from 0 to length of string s
            current = "" # current string we are comparing
            currentLength = 0
            for j in range(i, len(s)): # for loop, from i + 1 to length
                if s[j:j + 1] in current: # checking if the character is in the current string s[i:j] is the substring from index i to j
                    break
                current += s[j:j + 1] # add to current string
                currentLength += 1 # add one to the current length
            if currentLength > longestLength: # filters out longest length
                longestLength = currentLength
        return longestLength # returns longest length
            



        