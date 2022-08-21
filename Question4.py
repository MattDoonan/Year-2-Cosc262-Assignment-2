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
    
        
def line_edits(s1, s2):
    """Make s1 = s2 using edit distance"""    
    s1, s2 = s1.splitlines(), s2.splitlines()
    costlist = getCostList(s1,s2)
    finalresult = fr(s1,s2,costlist)
    return reversed(finalresult)

def ex(line,seq):
    """get S"""
    extra = []
    word = ''
    l1 = [char for char in line]
    l2 = [char for char in seq]    
    for c in l1:
        if len(l2) != 0 and l2[0] == c:
            word = word + l2.pop(0)
            if c == l1[-1]:
                extra.append(word)                
        else:
            if word != '':
                extra.append(word)
                word = ''
            extra.append(c)
    final = ''    
    for i in extra:
        if i in seq:
            final = final + i
        else:
            final = final + f"[[{i}]]"
    return final
            
def fr(s1,s2,costlist):
    """result"""
    y = len(costlist)-1
    x = len(costlist[0])-1
    finalresult = []  
    while x > 0 or y > 0:
        if len(s1) > 0 and len(s2) > 0 and y-1 >= 0 and x-1 >= 0 and s2[x-1] == s1[y-1]:
            finalresult.append(('C', s1[y-1], s2[x-1]))
            y-=1
            x-=1
        else:
            top = costlist[y-1][x]
            corner = costlist[y-1][x-1]
            minimum = min(costlist[y][x-1],top,corner)
            if y-1 >= 0 and x-1 >= 0 and minimum == corner:
                common = lcs(s1[y-1],s2[x-1])              
                finalresult.append(('S', ex(s1[y-1],common), ex(s2[x-1],common)))     
                y-=1
                x-=1
            elif y-1 >= 0 and minimum == top:
                finalresult.append(('D', s1[y-1], '')) 
                y-=1
            else:
                finalresult.append(('I', '', s2[x-1]))
                x-=1    
    return finalresult

def getCostList(s1,s2):
    """Make s1 = s2 using edit distance"""
    costlist = [[None for i in range(len(s2)+1)] for i in range(len(s1)+1)]
    for y in range(len(costlist)):
        for x in range(len(costlist[y])):
            if x == 0:
                costlist[y][x] = y
            elif y == 0:
                costlist[y][x] = x
            elif s2[x-1] == s1[y-1]:
                costlist[y][x] = costlist[y-1][x-1]
            else:
                costlist[y][x] = min(costlist[y-1][x],costlist[y][x-1],costlist[y-1][x-1])+1    
    return costlist
  
#Example
s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
