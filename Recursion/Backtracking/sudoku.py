from collections import defaultdict



"""
row=[0,1,1,1,0,-1,-1,-1]; col=[-1,-1,0,1,1,1,0,-1]
def is_safe(i,j,key,grid):
    p=(i//3)*3;q=(j//3)*3
    for ei in range(p,p+3):
        for ej in range(q,q+3):
            if grid[ei][ej]==key:
                return False
    for k in range(8):
        x=i+row[k];y=i+col[k]
        while x>=0 and y>=0 and x<9 and y<9:
            if grid[x][y]==key: return False
    return True 
"""

def next_pos(grid,store):
    for i in range(9):
        for j in range(9):
            if grid[i][j]=='.':
                store[0],store[1]=i,j
                return True
    return False

def assign(grid,row,col):
    for i in range(9):
        for j in range(9):
            if grid[i][j]!='.':
                row[i].add(grid[i][j])
                col[j].add(grid[i][j])

def is_safe(i,j,row,col,key,grid):
    if key in row[i]: return False
    if key in col[j]: return False
    ni=(i//3)*3;nj=(j//3)*3
    for p in range(3):
        for q in range(3):
            if grid[p+ni][q+nj]==key:
                return False
    return True


def sudoku_solver(grid,row,col):
    

    store=[0,0]
    if not next_pos(grid,store):
        return True

    r,c=store[0],store[1]

    for i in range(1,10):
        if is_safe(r,c,row,col,str(i),grid):

            grid[r][c]=str(i); row[r].add(str(i)); col[c].add(str(i))
            if sudoku_solver(grid,row,col):
                return True
            grid[r][c]='.'; row[r].remove(str(i)); col[c].remove(str(i))
    return False








if __name__=="__main__":
    grid=[["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
    row=defaultdict(set); col=defaultdict(set)
    assign(grid,row,col)
    print(sudoku_solver(grid,row,col))
    print(grid)