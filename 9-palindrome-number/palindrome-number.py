class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        s = str(x)
        rs = ''.join(reversed(s))
        if rs == x:
            return True
        return False