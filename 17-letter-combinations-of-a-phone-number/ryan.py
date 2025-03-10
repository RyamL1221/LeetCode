# Runtime: 0ms (100.00%), Memory: 12.35MB (83.53%)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, current):
            if index == len(digits):
                result.append("".join(current))
                return
            
            possible_letters = phone[digits[index]]
            for letter in possible_letters:
                current.append(letter)
                backtrack(index + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result
        
