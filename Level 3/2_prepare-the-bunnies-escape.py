"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
11
"""

def is_legal_move(y,x,map,visited,is_wr):
    if y < 0 or y >= len(map):
        return False
    if x < 0 or x >= len(map[y]):
        return False
    if visited[is_wr][y][x]: return False
    if map[y][x] == 1 and is_wr: return False
    return True

def solution(map):
    visited = [[[False for i in map[0]] for i in map],[[False for i in map[0]] for i in map]]
    visited[0][0][0] = True
    visited[1][0][0] = True
    
    distance = [[[0 for i in map[0]] for i in map],[[0 for i in map[0]] for i in map]]

    queue = []
    queue.append((0,0,False))
    
    while len(queue) != 0:
        curr = queue.pop(0)
        
        y = curr[0]
        x = curr[1]
        is_wr = curr[2]
        
        if y + 1 == len(map) and x + 1 == len(map[0]):
            return distance[is_wr][y][x] + 1

        #move right
        if is_legal_move(y,x + 1,map,visited,is_wr):
            new_is_wr = True if map[y][x + 1] == 1 else is_wr
            queue.append((y,x + 1,new_is_wr))
            distance[new_is_wr][y][x + 1] = distance[is_wr][curr[0]][curr[1]] + 1
            visited[new_is_wr][y][x + 1] = 1

        #move down
        if is_legal_move(y + 1,x,map,visited,is_wr):
            new_is_wr = True if map[y + 1][x] == 1 else is_wr
            queue.append((y + 1,x,new_is_wr))
            distance[new_is_wr][y + 1][x] = distance[is_wr][curr[0]][curr[1]] + 1
            visited[new_is_wr][y + 1][x] = 1

        #move left
        if is_legal_move(y,x - 1,map,visited,is_wr):
            new_is_wr = True if map[y][x - 1] == 1 else is_wr
            queue.append((y,x - 1,new_is_wr))
            distance[new_is_wr][y][x - 1] = distance[is_wr][curr[0]][curr[1]] + 1
            visited[new_is_wr][y][x - 1] = 1

        #move up
        if is_legal_move(y - 1,x,map,visited,is_wr):
            new_is_wr = True if map[y - 1][x] == 1 else is_wr
            queue.append((y - 1,x,new_is_wr))
            distance[new_is_wr][y - 1][x] = distance[is_wr][curr[0]][curr[1]] + 1
            visited[new_is_wr][y - 1][x] = 1

    return 0
