# Runtime: 0ms (100.00%), Memory: 18.08MB (10.42%)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            match s[i]:
                case '(':
                    stack.append('(')
                case ')':
                    if len(stack) < 1 or stack.pop() != '(':
                        return False
                case '{':
                    stack.append('{')
                case '}':
                    if len(stack) < 1 or stack.pop() != '{':
                        return False
                case '[':
                    stack.append('[')
                case ']':
                    if len(stack) < 1 or stack.pop() != '[':
                        return False
        
        if len(stack) > 0:
            return False
        else:
            return True
