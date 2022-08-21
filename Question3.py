def line_edits(s1, s2):
    """Make s1 = s2 using edit distance"""    
    s1, s2 = s1.splitlines(), s2.splitlines()
    costlist = getCostList(s1,s2)
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
                finalresult.append(('S', s1[y-1], s2[x-1]))     
                y-=1
                x-=1
            elif y-1 >= 0 and minimum == top:
                finalresult.append(('D', s1[y-1], '')) 
                y-=1
            else:
                finalresult.append(('I', '', s2[x-1]))
                x-=1
    return reversed(finalresult)

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
s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
