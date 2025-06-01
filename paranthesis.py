class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        for x in s:
            if (len(arr) > 0) and ((arr[len(arr)-1] == '(' and x == ')') or (arr[len(arr)-1] == '[' and x == ']') or (arr[len(arr)-1] == '{' and x == '}')):
                arr.pop()
            else:
                arr.append(x)
        return len(arr) == 0

print(Solution().isValid("()"))