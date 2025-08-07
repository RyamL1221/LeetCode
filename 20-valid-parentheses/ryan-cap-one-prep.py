# Runtime: O(n) 4ms (8.73%); Memory: O(n) 18.10MB (9.97%)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case '(':
                    stack.append('(')
                case ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                case '[':
                    stack.append('[')
                case ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
                case '{':
                    stack.append('{')
                case '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
                case _:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True
