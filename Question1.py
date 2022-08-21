def lcs(s1, s2):
    """Longest common subsequence bottom up"""
    letterlist = [[0 for i in range(len(s1)+1)] for i in range(len(s2)+1)]
    for y in range(1,len(letterlist)):
        for x in range(1,len(letterlist[y])):
            if s1[x-1] == s2[y-1]:
                letterlist[y][x] = letterlist[y-1][x-1] + 1
            else:
                change = max(letterlist[y][x-1], letterlist[y-1][x])
                letterlist[y][x] = change
    y = len(letterlist)-1
    x = len(letterlist[0])-1
    final_string = '' 
    while x > 0 and y > 0:
        if s1[x-1] == s2[y-1]:
            final_string = s1[x-1]+final_string
            y-=1
            x-=1
        else:
            left = letterlist[y][x-1]
            top = letterlist[y-1][x]
            if left <= top:
                y-=1
            else:
                x-=1
    return final_string
    
#Example
s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))
