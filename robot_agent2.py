def direction(x,y,m,n,up,down,left,right): # function that returns the possible direction for the agent
    if x<m-1:
        down=True
    if x>0:
        up=True
    if y<n-1:
        right=True
    if y>0:
        left=True
    return up,down,left,right

def set_valid(x,y,up,down,left,right,up_valid,down_valid,left_valid,right_valid): # function that returns the valid directions
    if up==True:
        if array[x-1][y]!=0 :
            up_valid=True
    if down==True:
        if array[x+1][y]!=0:
            down_valid=True
    if left==True:
        if array[x][y-1]!=0:
            left_valid=True
    if right==True:
        if array[x][y+1]!=0:
            right_valid=True
    return up_valid,down_valid,left_valid,right_valid

def traverse(l,k,array,x,y,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid): # we use this function to recursively traverse through the environment and backtrack
    up,down,left,right=direction(x,y,m,n,up=False,down=False,left=False,right=False)
    if(xd-x<0):
        down=False
    elif(xd-x>0):
        up=False
    up_valid,down_valid,left_valid,right_valid=set_valid(x,y,up,down,left,right,up_valid=False,down_valid=False,left_valid=False,right_valid=False)
    if up_valid==True:
        if x==xd and y==yd:
            print(l)
            visited[x][y]=False
            k=k+1
            return k
        if visited[x-1][y]!=True:
            visited[x-1][y]=True
            l.append(array[x-1][y])
            k=traverse(l,k,array,x-1,y,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid)
            del l[-1] # delete the last element while backtracking

    if down_valid==True:
        if x==xd and y==yd:
            print(l)
            k=k+1
            visited[x][y]=False
            return k
        if visited[x+1][y]!=True:
            visited[x+1][y]=True
            l.append(array[x+1][y])
            k=traverse(l,k,array,x+1,y,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid)
            del l[-1]

    if left_valid==True:
        if x==xd and y==yd:
            print(l)
            k=k+1
            visited[x][y]=False
            return k
        if visited[x][y-1]!=True:
            visited[x][y-1]=True
            l.append(array[x][y-1])
            k=traverse(l,k,array,x,y-1,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid)
            del l[-1]

    if right_valid==True:
        if x==xd and y==yd:
            print(l)
            k=k+1
            visited[x][y]=False
            return k
        if visited[x][y+1]!=True:
            visited[x][y+1]=True
            l.append(array[x][y+1])
            k=traverse(l,k,array,x,y+1,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid)
            del l[-1]
    visited[x][y]=False
    return k
# the environment
array=[[131,129,127,125,123,121,119, 0   , 0  ,  0],
       [10 ,11 ,12 ,13 ,14 ,15 , 16, 17  , 39 ,117], 
       [0  ,0  , 0 ,  0, 0 , 19, 20, 0   , 21 , 115],
       [0  ,0  , 0 , 22, 0 , 23, 24, 0   , 25 ,  113],
       [0  ,0  ,26 , 27, 0 , 28, 29, 0   , 30 ,   0],
       [31 ,32 ,33 , 34, 35, 36, 37 ,0   , 38 ,   0],
       [1  ,2  ,101,103,105,107, 109, 111, 0  ,   0]]
# array that records the visited places in the environment.
# the rooms are all marked visited because the agent doesnt have to go inside the rooms to reach a room.
visited=[[True,True,True,True,True,True,True,False,False, False],
         [False,False,False,False,False,False,False,False,False,True],
         [False,False,False,False,False,False,False,False,False,True],
         [False,False,False,False,False,False,False,False,False,True],
         [False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False],
         [True,True,True,True,True,True,True,True,True,True]]

m=7
n=10
agent_loc=[5,0]
x=agent_loc[0]
y=agent_loc[1]
visited[x][y]=True
dest_loc=[0,5]
xd=dest_loc[0]
yd=dest_loc[1]
visited[xd][yd]=False
up,down,left,right=False,False,False,False
up_valid,down_valid,left_valid,right_valid=False,False,False,False
l=[1]
k=0
print("There is a robot at location [0,0], it picks up the mail from this location and delivers it to any specified room number")
print("All the possible paths the robot can travel through are:\n")

k=traverse(l,k,array,x,y,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid)
print("There are ",k," different paths that the robot can take")
