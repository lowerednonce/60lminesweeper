import random as r;winning=True;cbflags=0; print("Usage:\n  d <row>,<column> - dig at <row> <column>\n  f <row>,<column> - flag/unflag <row> <column>\n  q - quit\n")
a1=[[0 for x in range(10)] for y in range(10)]     # map
a2=[[False for x in range(10)] for y in range(10)] # shown
a3=[[False for x in range(10)] for y in range(10)] # flagged
def displaymap(full):
    global a1,a2,a3;print("  0 1 2 3 4 5 6 7 8 9 ")
    for x in range(len(a1[0])):
        t=str(x)+"|"
        for y in range(len(a2[0])):
            if(full and a3[x][y]):                        t+= "F "
            elif(full and a1[x][y]==-1):                  t+= "# "
            elif(full):                                   t+= str(a1[x][y])+" "
            elif(not full and a2[x][y]):                  t+= str(a1[x][y])+" "
            elif(not full and a3[x][y]):                  t+= "F "
            elif(not full and a2[x][y] and a1[x][y]==-1): t+= "# "
            else: t+= "X "
        print(t)
def f(x,y):
    global a1
    try:
        return a1[x][y]==-1
    except: pass
for i in range(10):
    x=r.randint(0,9); y=r.randint(0,9)
    while a1[x][y]!=0: x=r.randint(0,9); y=r.randint(0,9)
    if(a1[x][y]==0): a1[x][y]=-1
for x in range(len(a1[0])):
    for y in range(len(a1[x])):
        if(a1[x][y]==-1): continue
        if(f(x-1,y+1)): a1[x][y]+=1
        if(f(x,  y+1)): a1[x][y]+=1
        if(f(x,  y+1)): a1[x][y]+=1
        if(f(x+1,y+1)): a1[x][y]+=1
        if(f(x-1,  y)): a1[x][y]+=1
        if(f(x+1,  y)): a1[x][y]+=1
        if(f(x-1,y-1)): a1[x][y]+=1
        if(f(x,  y-1)): a1[x][y]+=1
        if(f(x+1,y-1)): a1[x][y]+=1
while winning:
    displaymap(False);c=raw_input(">").split(" ")
    if(c[0]=="f"):   a3[int(c[1].split(',')[0])][int(c[1].split(',')[1])]=not a3[int(c[1].split(',')[0])][int(c[1].split(',')[1])]
    if(c[0]=="f" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==-1): cbflags+=1
    if(c[0]=="f" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]!=-1): cbflags-=1
    if(c[0]=="f" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==-1 and a3[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==True): cbflags-=1
    if(c[0]=="d" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==-1): winning=False
    if(c[0]=="d"):   a2[int(c[1].split(',')[0])][int(c[1].split(',')[1])]=True
    if(c[0]=="d" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==0):
        try:
            a2[x-1][y+1]=True; a2[x][y+1]=True; a2[x+1][y+1]=True; a2[x-1][y]=True; a2[x+1][y]=True
            a2[x-1][y-1]=True; a2[x][y-1]=True; a2[x+1][y-1]=True;
        except: pass
    if(cbflags==10): winning = False
    if(c[0]=="q"): exit()
if(cbflags==10): print("----You've won----")
else: print("----You've lost---")
displaymap(True)
