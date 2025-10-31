class Solution(object):
    def getRomanValue(self, b):
        hsh = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        return hsh[b]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        sum = 0
        for i in range(n-1, -1, -1):
            a = self.getRomanValue(s[i])
            b = self.getRomanValue(s[i-1])
            if b < a:
                sum += a-b
            else:
                sum += a
        return sum

Solution().romanToInt('LVIII')
        