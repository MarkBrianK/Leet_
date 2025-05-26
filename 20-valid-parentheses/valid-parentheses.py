class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')' : '(', '}':'{', ']':'['}
        stck = []

        for char in s:
            if char in brackets:
                if not stck or stck[-1] != brackets[char]:
                    return False
                stck.pop()
            else:
                stck.append(char)
        
        return len(stck) == 0
