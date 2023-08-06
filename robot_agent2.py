def direction(x,y,m,n,up,down,left,right): # this function gives the possible directions that the agent can move to
    if x<m-1:
        down=True
    if x>0:
        up=True
    if y<n-1:
        right=True
    if y>0:
        left=True
    return up,down,left,right

def set_valid(x,y,up,down,left,right,up_valid,down_valid,left_valid,right_valid): # this function senses the restricted areas, and returns only the valid directions
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

def traverse(l,k,array,x,y,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid): # this function is used for backtracking through recursion
    up,down,left,right=direction(x,y,m,n,up=False,down=False,left=False,right=False)
    if(xd-x<0):
        down=False
    elif(xd-x>0):
        up=False
    up_valid,down_valid,left_valid,right_valid=set_valid(x,y,up,down,left,right,up_valid=False,down_valid=False,left_valid=False,right_valid=False)

    if up_valid==True:
        if x==xd and y==yd: # to check if the current location is the destination location
            print(l)
            k=k+1
            visited[x][y]=False
            return k
        if visited[x-1][y]!=True: # checks if a certain location has already been visited
            visited[x-1][y]=True
            l.append(array[x-1][y])
            k=traverse(l,k,array,x-1,y,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid) # recursion
            del l[-1] # deleting the last element while backtracking

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

# environment
array=[[131,129,127,125,123,121,119 ,0],
       [10 ,11 ,12 ,13 ,14 ,15 , 16 ,117],
       [0  ,0  , 0 ,  0, 0,  0, 18 , 115],
       [0  ,0  , 0 ,  0, 19, 20, 21 , 113],
       [0  ,0  , 0 , 22, 23, 24, 25 ,  0],
       [0  ,0  ,26 , 27, 28, 29, 30 ,  0],
       [1  ,2  ,101,103,105,107, 109,111]]

visited=[[False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False],
         [True,False,False,False,False,False,False,False]]
         
m=7 #rows
n=8 #columns
agent_loc=[6,0] # current location
x=agent_loc[0]
y=agent_loc[1]
dest_loc=[0,5] # destination
xd=dest_loc[0]
yd=dest_loc[1]
up,down,left,right=False,False,False,False
up_valid,down_valid,left_valid,right_valid=False,False,False,False
l=[1]
k=0

print("There is a robot at location [0,0], it picks up the mail from this location and delivers it to any specified room number")
print("All the possible paths the robot can travel through are:\n")
k=traverse(l,k,array,x,y,xd,yd,visited,m,n,up,down,left,right,up_valid,down_valid,left_valid,right_valid)
print("There are ",k," different paths that the robot can take")
