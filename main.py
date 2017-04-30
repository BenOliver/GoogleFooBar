#google tryouts

import cProfile
#from test import test_getargs2

def myElevator(l):
    l=[x.split('.') for x in l]
    for n,i in enumerate(l):
        print i
        l[n]=[int(k) for k in i]
        print i
        #for j,k in enumerate(i):
        #    i[j]=int(k)
            
    print('preSort:{}'.format(l))
    l.sort()
    print('postSort:{}'.format(l))
    for n,i in enumerate(l):
        l[n]='.'.join([str(j) for j in i])
    
    return l

def bunnyCounter(x,y):
    def seriesSum(start,end):
        #sum of an arithmatic series
        return (start+end)*(abs(start-end)+1)/2
    return seriesSum(x,1)+seriesSum(x,x+y-2) 
    
    #id_Num=0
    #id_Num=id_Num+seriesSum(x,1)+ser
    #calculate sum of series: x, x-1,x-2,...1
    #while i>0:
    #    id_Num+=i
    #    i-=1
    
    #calculate sum of series: x,x+1,x+2,x+(y-2)
    #if y>1:
    #    for i in range(y-1):
    #        id_Num+=i
    #return str(id_Num)
  
    # your code here

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
            
def queueToDo(start,length,fast=False):
    
    def sequenXOR(*args):
        if len(args)==1:
            num=args[0]
            #print('num is:{}'.format(num))
            n=0
            b=2**n
            xor=0
            while(b<=num):
                #print('b is :{}'.format(b))
                #B 
                B=num//b
                #print('B is :{}'.format(B))
                if n==0:
                    z=((num+1)//2)%2
                else:
                    if B%2:
                        z=(num-b*B+1)%2    
                    else:
                        z=0
                #print('z is :{}'.format(z))
                if z:
                    xor=xor^b
                #print('xor is :{}'.format(xor))
                n+=1
                b=2**n
            return xor
        elif len(args)==2:
            upper=max(args)
            lower=min(args)
            return sequenXOR(upper)^sequenXOR(max(0,lower-1))
            
     
    val=start
    #seperate variable for length of row
    rowLength=length
    row=0
    xor=0
    
    #print('answer is:{}'.format(sequenXOR(2000,3)))
    if fast:
        while(row<length):
            indx=0
            beg=val
            end=val+rowLength-1
            #print('beggining:{},\tend:{}'.format(beg,end))
            xor=xor^(sequenXOR(beg,end))
            val=end+1+row
            row+=1
            rowLength-=1
            
    else:
        while(row<length):
            #reset index to 0 at start of row
            indx=0
            while(indx<rowLength):
                #print('index:{}\trow:{}\tval:{}'.format(indx,row,val))
                #lst.append(val)
                xor=xor^val
                val+=(1)
                indx+=1
            #increment val by the row value
            val+=row
            row+=1
            #shorten row length
            rowLength-=1
        
        #print(lst)
        #perform checksum on all values
    #     for i in lst:
    #         xor=xor^i
        #print xor
    return xor
        
def stairCounter(bricks):
    
    soluArray=[[0]]*201
    #keep a record of solved steps to speed computation
    for j,row in enumerate(soluArray):
        soluArray[j]=[-1]*201
        
    
    def stairCounterRec(bricks,prevStepSize=None):
        '''this function uses the number of bricks as input
        and returns the number of solutions that can be achieved
        '''
        if prevStepSize==None:
            #if at the beginning of the sequence
            stepSize=bricks-1
        else:
            #otherwise decrement the stepsize down one, or to the number of bricks remaining
            stepSize=min(prevStepSize-1,bricks)
            
            
            
        #check if solution is already done
        if soluArray[bricks][stepSize]>=0:
            return soluArray[bricks][stepSize]
            
        #calculate smallest step possible to complete staircase
        lim=(2*bricks+0.25)**0.5-0.5
        
        #print('lim is {}'.format(lim))

        if stepSize<lim:
            #cannot complete staircase
            return 0
        if bricks==1:
            #print('bricks:{}'.format(bricks))
            if stepSize>=1:
                return 1
            else:
                #staircase complete yet bricks are remaining
                return 0
        elif bricks==0:
            return 1
        solutionCount=0
        origStep=stepSize
        while(stepSize>=lim):
            #print('stepSize:{}\nbricks:{}'.format(stepSize,bricks))
            solutionCount+=stairCounterRec(bricks-stepSize,stepSize)
            #print('stepSize {}, lim {:.2f}, {} bricks, gives {} solutions'.format(origStep,lim,bricks,solutionCount))
            stepSize-=1
        #print('stepSize {}, lim {:.2f}, {} bricks, gives {} solutions'.format(prevStepSize-1,lim,bricks,solutionCount))
        if bricks<origStep:
            soluArray[bricks][origStep:]=[solutionCount]*len(soluArray[bricks][origStep:])
        else:
            soluArray[bricks][origStep]=solutionCount
        

        return solutionCount
    
    return stairCounterRec(bricks)


def main():
    #print(myEncrypt("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
    #print(myEncrypt("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
    #myL=["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2","1.0","1","1.0.0"]
    #myL=["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
    #print(myElevator(myL))
    #print(myL)
    #print(bunnyCounter(3,2))
    #mat=[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
#     mat=[[0, 0, 0, 0, 0, 0, 0],\
#          [1, 1, 1, 1, 1, 1, 0],\
#          [1, 0, 0, 0, 0, 0, 0],\
#          [0, 1, 1, 1, 1, 1, 0],\
#          [0, 1, 1, 1, 1, 1, 1],\
#          [0, 0, 0, 0, 0, 0, 1],
#          [0, 0, 0, 0, 0, 0, 0]]
    #mat=[[0,1],[1,0]]
#     print('answer is:{}'.format(mazeSolver(mat)))

#     cProfile.run('queueToDo(17,2000,fast=True)')
#     print('fast:\t{}'.format(queueToDo(17,2000,fast=True)))
#     cProfile.run('queueToDo(17,2000)')
#     print('slow:\t{}'.format(queueToDo(17,2000)))
    print(stairCounter(200))
    
    


if __name__=='__main__':
    main()
