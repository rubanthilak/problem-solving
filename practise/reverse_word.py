def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        arr=[]
        n=len(s)
        i=n-1
        j=i
        while i>-1:
            if (s[i-1]==' ' or i-1 == -1) and s[i] != ' ':
                arr.append(s[i:j+1])
            elif s[i-1]!=' ' and s[i] == ' ':
                j=i-1
            i-=1
        return ' '.join(arr)

res=reverseWords("the sky is blue")
print(res)