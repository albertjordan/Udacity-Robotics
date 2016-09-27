# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
            [8, 7, 6, 5, 4, 3],
            [7, 6, 5, 4, 3, 2],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1, 0]]



expand = []
for x in range(len(grid)):
    row = []
    for y in range(len(grid[0])):
        row.append(-1)
    expand.append(row)
    

expand[0][0] = 0

print expand

goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1


def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    
    goalRow = len(grid) - 1
    goalColumn = len(grid[0]) - 1

    openList = []           # list of open nodes
    counter = 0
    f = counter + heuristic[0][0]
    init = [f, 0, 0, 0]
    openList.append(init)
    grid[init[2]][init[3]] = 1
    

    step = 0
    path = [f, 0, 0, 0]

#    printGrid()

    counter = 0
    f = 0 + heuristic[0][0]
    step = 0

    while (len(openList) > 0):

        items = len(openList)
        print "openList:", openList
        newList = []
        counter += 1

        for i in range(items):
            print "openList:",openList
            openList.sort()
            #openList.reverse()
            print "sorted:",openList
            openList.reverse()
            print "reverse:",openList
            node = openList.pop()
            print "node:",node
            row = node[2]
            column = node[3]
            
            step += 1

            
            expand[row][column] = step 

                 
#            print 'checking ', node

            if ( (row == goalRow) and (column == goalColumn) ):
                path = [counter, row, column]
#                print path
#                print 'done'
                return path
            ##  expand 

            for j in range(len(delta)):
                y = row + delta[j][0]
                x = column + delta[j][1]
                

                if ( x < 0 or x == len(grid[0])):
                    continue  # out of bounds
                if ( y < 0 or y == len(grid)):
                    continue # out of bounds
                if ( grid[y][x] == 1 ):
                    continue # already occupied

                # else add to the list
                
                print "exapnding: ", y, ",",x
                
                f = counter + 1 + heuristic[y][x]
                
                #newList.append([f,counter,y,x])
                
                openList.insert(0, [f,counter + 1,y,x])
                
#                step += 1
                
#                 expand[y][x] = step 

                # mark the grid
                grid[y][x] = 1
#                printGrid()

#        counter += 1
        
        #openList = newList
#        openList.insert(0, newList)
        print 'NEW openlist:',openList
#        print 'open list is: ', openList                            


    return 'fail'  # you should RETURN your result

print search()


for i in range(len(expand)):
    print expand[i]
    
