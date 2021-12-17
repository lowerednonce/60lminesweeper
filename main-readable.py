import random as r
winning=True
cbflags=0
print("""Usage:
  d <row>,<column> - dig at <row> <column>
  f <row>,<column> - flag/unflag <row> <column>
  q - quit
""")
a1=[[0 for x in range(10)] for y in range(10)]     # the map is stored in this array, -1 means mine, other values are supposed to indicate the number of neighboring  mines
a2=[[False for x in range(10)] for y in range(10)] # the array used to store which areas of the map are shown
a3=[[False for x in range(10)] for y in range(10)] # the array used to store the flags
def displaymap(full):
    global a1,a2,a3
    print("  0 1 2 3 4 5 6 7 8 9 ") # header
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
  # access the specified mine and return whether it is a mine, if the requested location is outside the array, do nothing
    global a1
    try:
        return a1[x][y]==-1
    except: pass # no exeption handling
for i in range(10):
   # fill the map up with 10 mines
    x=r.randint(0,9)
    y=r.randint(0,9)
    while a1[x][y]!=0:
      x=r.randint(0,9)
      y=r.randint(0,9)
    if(a1[x][y]==0): 
      a1[x][y]=-1
# choose a random location until it isn't occupied (this is to prevent mines from stacking up) and place it with a1
for x in range(len(a1[0])):
    for y in range(len(a1[x])):
      # fill a1 up with the needed number
        if(a1[x][y]==-1): continue # if the given cell is a mine, ignore it
        if(f(x-1,y+1)): a1[x][y]+=1
        if(f(x,  y+1)): a1[x][y]+=1
        if(f(x,  y+1)): a1[x][y]+=1
        if(f(x+1,y+1)): a1[x][y]+=1
        if(f(x-1,  y)): a1[x][y]+=1
        if(f(x+1,  y)): a1[x][y]+=1
        if(f(x-1,y-1)): a1[x][y]+=1
        if(f(x,  y-1)): a1[x][y]+=1
        if(f(x+1,y-1)): a1[x][y]+=1
        # these checked for all the fields next to the given field for mines
while winning:
  # main game loop
    displaymap(False) # the False is to only display shown maps stored in a3 
    c=raw_input(">").split(" ") # split the input by a space when got
    if(c[0]=="f"):
      # flip the flagged status with the not kevword
      a3[int(c[1].split(',')[0])][int(c[1].split(',')[1])]=not a3[int(c[1].split(',')[0])][int(c[1].split(',')[1])]
    if(c[0]=="f" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==-1): cbflags+=1
    if(c[0]=="f" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]!=-1): cbflags-=1
    if(c[0]=="f" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==-1 and a3[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==True): cbflags-=1
    # if the flag is right, increase cbflags, if it's wrong decrease it, if you unflag the right mine, decrease it
    if(c[0]=="d" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==-1):
      winning=False # if you dig on a mine, you die
    if(c[0]=="d"):
      a2[int(c[1].split(',')[0])][int(c[1].split(',')[1])]=True
      # set any digged field to show, doesn't matter if the winning is False, as the next map display is going to be with the True flag out of the main game loop
    if(c[0]=="d" and a1[int(c[1].split(',')[0])][int(c[1].split(',')[1])]==0):
        try:
            a2[x-1][y+1]=True
            a2[x][y+1]  =True
            a2[x+1][y+1]=True
            a2[x-1][y]  =True
            a2[x+1][y]  =True
            a2[x-1][y-1]=True
            a2[x][y-1]  =True
            a2[x+1][y-1]=True
        except: pass
        # clear neighboring fields when dug on a 0
    if(cbflags==10): winning = False
    if(c[0]=="q"): exit()
if(cbflags==10):
  print("----You've won----")
else:
  print("----You've lost---")
displaymap(True)
#display map without caring about a3
