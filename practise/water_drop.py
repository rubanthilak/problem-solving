def trap(height) -> int:
    n=len(height)
    prefix=[0]*n
    suffix=[0]*n
    mx=0
    for i in range(1, n):
        l=i-1
        r=i+1
        while l>= 0:
            if height[l]>prefix[i]:
                prefix[i]=height[l]
            l-=1
        while r<n:
            if height[r]>suffix[i]:
                suffix[i]=height[r]
            r+=1
    for i in range(1, n-1):
        if height[i] < prefix[i] and height[i] < suffix[i]:
            mx += min(prefix[i], suffix[i]) - height[i]
    return mx

height=[0,2,0,3,1,0,1,3,2,1]
res=trap(height)
print(res)