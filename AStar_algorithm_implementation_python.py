''' 
f = g + h
f = node cost
g = cost to get to current node from start node
h = heuristic (estimated distance to destination)


'''
import heapq

class Node:    
    def __init__(self, x, y, destination, costSoFar):
        self.x = x
        self.y = y
        self.costSoFar = costSoFar
        if (destination != None):
            self.h = (destination.x - x)**2 + (destination.y - y)**2
            self.g = costSoFar
            if (self.h == 0):
                self.g = 0
            self.f = self.g + self.h

def CheckIfInList(a, list):
    for element in list:
        if (element[0] == a.f):
            if(a.x == element[2].x and a.y == element[2].y):
                return True
    return False

def AddUniqueToList(a, unprocessed, path, grid, itemid):
    if(grid[a.x][a.y] == 0 and a.x >=0 and a.y >=0):
        if(not CheckIfInList(a, unprocessed)and not CheckIfInList(a,path)):
            heapq.heappush(unprocessed, (a.f,itemid, a))
def AStar (start, destination, grid):
    unprocessed = [(start.f, 0, start)]
    path = []
    itemid = 1
    while len(unprocessed) > 0:
        current = unprocessed[0]
        current = current[2]
        if(current.x == destination.x and current.y == destination.y):
            #complete, backtrack through unprocessed.
            print("Done")
            unprocessed.clear()
        else:
            path.append((current.f,0,current))
            newNode = Node(current.x+1, current.y+1, destination, current.costSoFar+1)
            AddUniqueToList(newNode,unprocessed, path, grid,itemid)
            itemid += 1
            newNode = Node(current.x+1, current.y, destination, current.costSoFar+1)
            AddUniqueToList(newNode,unprocessed, path, grid,itemid)
            itemid += 1
            newNode = Node(current.x+1, current.y-1, destination, current.costSoFar+1)
            AddUniqueToList(newNode,unprocessed, path, grid,itemid)
            itemid += 1
            newNode = Node(current.x, current.y+1, destination, current.costSoFar+1)
            AddUniqueToList(newNode,unprocessed, path, grid,itemid)
            itemid += 1
            newNode = Node(current.x, current.y-1, destination, current.costSoFar+1)
            AddUniqueToList(newNode,unprocessed, path, grid,itemid)
            itemid += 1
            newNode = Node(current.x-1, current.y+1, destination, current.costSoFar+1)
            AddUniqueToList(newNode,unprocessed, path, grid,itemid)
            itemid += 1
            newNode = Node(current.x-1, current.y, destination, current.costSoFar+1)
            AddUniqueToList(newNode,unprocessed, path, grid,itemid)
            itemid += 1
            newNode = Node(current.x-1, current.y-1, destination, current.costSoFar+1)
            AddUniqueToList(newNode,unprocessed, path, grid,itemid)
            itemid += 1

destination = Node(1,4,None, 0)
start = Node(0,0, destination, 0)
#0 represents an open point, 1 represents a blocked point
grid = [[0,0,0,0,0],[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
AStar(start, destination, grid)

    