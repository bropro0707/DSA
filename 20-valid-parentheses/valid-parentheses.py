class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        stack = [''] * n
        top = -1
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                top += 1
                stack[top] = ch
            else:
                if top < 0:
                    return False
                last = stack[top]
                if (ch == ')' and last != '(') or \
                (ch == ']' and last != '[') or \
                (ch == '}' and last != '{'):
                    return False
                top -= 1
        return top == -1