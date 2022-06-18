def find_next_empty(puzzle):
    #find the next row,col on puzzle that's not yet filled --> rep with -1
    #return row,col tuple or (none,none)if there is none

    #keep in mind that we are using 0-8 four our indices
    for r in range(9):
        for c in range(9):# range(9) is o....8
            if puzzle[r][c] == -1:
                return r,c

    return None,None # if no spaces in puzzle are empty

def is_valid(puzzle, guess, row, col):
    #lets start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #now the column
    col_vals = []
    for i in range(9):
         col_vals.append(puzzle[i][col])
         if guess in col_vals:
             return False
    # now the square
    row_start =(row // 3) * 3
    col_start =(col // 3) * 3

    for r in range(row_start,row_start + 3):
        for c in range(col_start,col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # if we get here,these checks pass
    return True            

def solve_sudoku(puzzle):
    #solve sudoku using backtracking 
    #step1 : choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left,then we're done because we only allowed valid inputs
    if row is None:
        return True

    # step 2:if there is a place to put a number , then make a guess between 1 and 9
    for guess in range(1,10):
        #step 3: check if it is valid
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col] =  guess
            #now recurse using the puzzle
            #step4 : recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step5 : if not valid ,then we need backtrack
        puzzle[row][col] = -1 #reset the guess

    #step6 : puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = [

        [3,9,-1,  -1,5,-1,  -1,-1,-1],
        [-1,-1,-1,  2,-1,-1,  -1,-1,5],
        [-1,-1,-1,  7,1,9,  -1,8,-1],

        [-1,5,-1,  -1,6,8,  -1,-1,-1],
        [2,-1,6,  -1,-1,3,  -1,-1,-1],
        [-1,-1,-1,  -1,-1,-1,  -1,-1,4],

        [5,-1,-1,  -1,-1,-1,  -1,-1,-1],
        [6,7,-1,  1,-1,5,  -1,4,-1],
        [1,-1,9,  -1,-1,-1,  2,-1,-1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)    
