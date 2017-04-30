'''
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7

Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''
def mazeSolver(maze):

    def findPath(mat,X,Y,startX,startY):
        #calculate the path values from 0,0 to every point
        currentMin=99999

        #create an array to hold properties for each spot
        dictMat=[[None]]*Y
        for j in range(Y):
            dictMat[j]=[None]*X
            for i in range(X):
                dictMat[j][i]={'val':99999,'unMapped':True,'neighborFilled':False,'x':i,'y':j}
        #set start to value 1, flag as mapped, and add to in-progress list
        dictMat[startY][startX]['val']=1
        dictMat[startY][startX]['unMapped']=False
        inProg=[dictMat[startY][startX]]
        
        
        
        #iterate until no more left in progress
        while(len(inProg)>0):
            #print('-'*20)
            inProgTemp=[]
            for spot in inProg:
                x=spot['x']
                y=spot['y']
                for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if (i//X==0) & (j//Y==0): #check within bounds
                        target=dictMat[j][i]
                        #check if wall
                        if target['unMapped'] & mat[j][i]:
                            #set to mapped if target is a wall
                            #print('set {},{} as wall'.format(i,j))
                            target['unMapped']=False
                        if target['unMapped']:
                            #print('target is:\n\t{}'.format(target))
                            #add one to path and check if small than current path
                            target['val']=min(target['val'],spot['val']+1)
                            #add to inProg list
                            inProgTemp.append(target)
                spot['neighborFilled']=True

            for spot in inProgTemp:
                if spot not in inProg:
                        inProg.append(spot)
            currentValList=[spot['val'] for spot in inProg]
            currentMin=min(currentValList)
            for spot in inProg:
                if (spot['val']<=currentMin) & spot['neighborFilled']:
                    spot['unMapped']=False
                    inProg.remove(spot)

            
            #print(inProg)    
            #print('currenMin:{}'.format(currentMin))
            valMat=[[None]]*Y
            for j,row in enumerate(dictMat):
                valMat[j]=[i['val'] if i['val']<99999 else 0 for i in row]
        return valMat

    #make list of wall coordinates
    shortcutList=[]
    Y=len(maze)
    for y,row in enumerate(maze):
        X=len(row)
        for x,spot in enumerate(row):
            #if a wall is here
            if spot:
                #print('wall at {},{}'.format(x,y))
                #count adjacent spots which are empty
                spaces=[]
                for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    #if both oords are within bounds
                    if (i//X==0) & (j//Y==0):
                        #print('val at {},{} is {}'.format(i,y,mat[y][i]))
                        #add 1 if no wall
                        if maze[j][i]==0:
                            spaces.append((i,j))
                #check adjacent free spots are 2 or greater
                if len(spaces)>1:
                    for start in spaces:
                        spaces.remove(start)
                        for end in spaces:
                            shortcutList.append((start,end,(x,y)))


    print('OriginalMaze:')
    for i in maze:
        print(i)
    solvedMaze1=findPath(maze,X=X,Y=Y,startX=0,startY=0)
    solvedMaze2=findPath(maze,X=X,Y=Y,startX=X-1,startY=Y-1)
    paths=[]
    print('solvedMaze1:')
    for i in solvedMaze1:
        print(i)
    print('solvedMaze2:')
    for i in solvedMaze2:
        print(i)
    #print(shortcutList)
    for i in shortcutList:
        x1,y1=i[0]
        x2,y2=i[1]
        if (solvedMaze1[y1][x1] & solvedMaze2[y2][x2]):
            paths.append(solvedMaze1[y1][x1] + solvedMaze2[y2][x2]+1)
        elif (solvedMaze2[y1][x1] & solvedMaze1[y2][x2]):
            paths.append(solvedMaze2[y1][x1] + solvedMaze1[y2][x2]+1)
                
    minPath=min(paths)
    #elif 0:
    #    minPath=solvedMaze1[-1][-1]
    #    pathReduction=[]
    #    for i in shortcutList:
    #        x1,y1=i[0]
    #        x2,y2=i[1]
    #        shortcut1=abs(solvedMaze1[y2][x2]-solvedMaze1[y1][x1])-2
    #        pathReduction=pathReduction+[minPath-solvedMaze1[y1][x1].append(shortcut)]
    #    if len(pathReduction)>0:
    #        usedShortcut=max(pathReduction)
    #        print(usedShortcut)
    #        print(minPath)
    #        minPath=minPath-max(pathReduction)
        
    return(minPath)

#mat=[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
mat=[[0, 0, 0, 0, 0, 0, 0],\
    [1, 1, 1, 1, 1, 1, 0],\
    [1, 0, 0, 0, 0, 0, 0],\
    [0, 1, 1, 1, 1, 1, 0],\
    [0, 1, 1, 1, 1, 1, 1],\
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]]
#mat=[[0,1],[1,0]]
print('answer is:{}'.format(mazeSolver(mat)))