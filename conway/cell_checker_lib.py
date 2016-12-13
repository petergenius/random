def is_real(grid,x,y):
    height = len(grid)-1
    length = len(grid[0])-1
    if x >= 0 and x <= length and y >= 0 and y <= height:
        return True
    else:
        return False

def check_for_surrounding(grid,x, y, char):
    #grid looks like this: [[x,y,z],[a,b,c],[d,e,f]] | x=1, y=2 > e 
    count = 0
    if is_real(grid, x-1, y):
        if grid[y][x-1] == char:
            count += 1
    if is_real(grid, x+1, y):
        if grid[y][x+1] == char:
            count += 1
    if is_real(grid, x, y+1):
        if grid[y+1][x] == char:
            count += 1
    if is_real(grid, x, y-1):
        if grid[y-1][x] == char:
            count += 1
    if is_real(grid, x-1, y-1):
        if grid[y-1][x-1] == char:
            count += 1
    if is_real(grid, x+1, y+1):
        if grid[y+1][x+1] == char:
            count += 1
    if is_real(grid, x-1, y+1):
        if grid[y+1][x-1] == char:
            count += 1
    if is_real(grid, x+1, y-1):
        if grid[y-1][x+1] == char:
            count += 1
    return count

