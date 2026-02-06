# Python3 program to find minimum number of moves

from queue import Queue
n = 8
knightX = 2
knightY = 2

targetX = 5
targetY = 5

def isValid(currX , currY , n):
    if currX < 1 or currX > n:
        return False
    
    if currY < 1 or currY > n:
        return False
    return True

def minimumMove(n , targetX , targetY , knightX , knightY):
    nodes = Queue()
    vis = dict()
    possible = [(2,1) , (2,-1) , (-2,1) , (-2,-1) , (1,2) , (-1,2) ,(1,-2) ,  (-1,-2)]
    nodes.put((knightX , knightY , 0))
    vis[(knightX , knightY)] = 1

    while nodes.empty() == False:
        temp = nodes.get()
        currX = temp[0]
        currY = temp[1]
        currLevel = temp[2]

        print(currX , currY , currLevel)

        if currX == targetX and currY == targetY:
            return currLevel
        
        for i in possible:
            if isValid(currX + i[0], currY + i[1], n) == False or vis.get((currX + i[0] , currY + i[1])) == 1:
                continue

            vis[(currX + i[0] , currY + i[1])] = 1
            nodes.put((currX + i[0] , currY + i[1] , currLevel + 1))
    return -1
print(minimumMove(n , targetX , targetY , knightX , knightY))

