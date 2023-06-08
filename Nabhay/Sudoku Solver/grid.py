import time
import random
import copy

class Grid:

    def __init__(self,grid=[]):
        self.grid = grid
    
    def print(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end=" ")
            print()

    def print16x16(self):
        for i in range(16):
            for j in range(16):
                print(self.grid[i][j], end=" ")
            print()

    def print4x4(self):
        for i in range(16):
            for j in range(16):
                print(self.grid[i][j], end=" ")
            print()

    # check if a number is incorrect 
    def isok(self, grid, row, col, n):
        """Helper function"""
        #check if it's the only number in the grid
        for x in range(9):
            if grid[row][x] == n:
                return False
            if grid[x][col] == n:
                return False

        #check if it's the only number in it's 3x3 grid
        for y in range(3):
            for x in range(3):
                if grid[y + (row - row % 3)][x + (col - col % 3)] == n:
                    return False
        return True

    # check if a number is incorrect 
    def isok16x16(self, grid, row, col, n):
        """Helper function"""
        #check if it's the only number in the grid
        for x in range(16):
            if grid[row][x] == n:
                return False
            if grid[x][col] == n:
                return False

        #check if it's the only number in it's 3x3 grid
        for y in range(4):
            for x in range(4):
                if grid[y + (row - row % 4)][x + (col - col % 4)] == n:
                    return False
        return True

    # check if a number is incorrect 
    def isok4x4(self, grid, row, col, n):
        """Helper function"""
        #check if it's the only number in the grid
        for x in range(4):
            if grid[row][x] == n:
                return False
            if grid[x][col] == n:
                return False

        #check if it's the only number in it's 3x3 grid
        for y in range(2):
            for x in range(2):
                if grid[y + (row - row % 2)][x + (col - col % 2)] == n:
                    return False
        return True
    
    def set_rand_grid(self):
    
        base = 3
        side  = 3*3

        def pattern(r,c):
            return (3*(r%3)+r//3+c)%side

        def shuffle(s):
            return random.sample(s,len(s)) 
        random_base = range(3) 
        rows  = [ g*3 + r for g in shuffle(random_base) for r in shuffle(random_base) ] 
        cols  = [ g*3 + c for g in shuffle(random_base) for c in shuffle(random_base) ]
        nums  = shuffle(range(1,3*3+1))

        self.grid = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        squares = side*side
        empties = 51
        for p in random.sample(range(squares),empties):
            self.grid[p//side][p%side] = 0

    def set_rand_grid16x16(self):
    
        base = 4
        side  = 4*4

        def pattern(r,c):
            return (4*(r%4)+r//4+c)%side

        def shuffle(s):
            return random.sample(s,len(s)) 
        random_base = range(4) 
        rows  = [ g*4 + r for g in shuffle(random_base) for r in shuffle(random_base) ] 
        cols  = [ g*4 + c for g in shuffle(random_base) for c in shuffle(random_base) ]
        nums  = shuffle(range(1,4*4+1))

        self.grid = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        squares = side*side
        empties = 110
        for p in random.sample(range(squares),empties):
            self.grid[p//side][p%side] = 0

    def set_rand_grid4x4(self):
    
        base = 2
        side  = 2*2

        def pattern(r,c):
            return (2*(r%2)+r//2+c)%side

        def shuffle(s):
            return random.sample(s,len(s)) 
        random_base = range(2) 
        rows  = [ g*2 + r for g in shuffle(random_base) for r in shuffle(random_base) ] 
        cols  = [ g*2 + c for g in shuffle(random_base) for c in shuffle(random_base) ]
        nums  = shuffle(range(1,2*2+1))

        self.grid = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        squares = side*side
        empties = 12
        for p in random.sample(range(squares),empties):
            self.grid[p//side][p%side] = 0

    # solve using bitmask
    def solve(self, grid, row=0, col=0):
        # if it oversteps the board just stop
        if row == 8 and col == 9:
            return True

        # lead it to the next row if it oversteps columns while checking
        if col == 9:
            row += 1
            col = 0

        # start a tree if there's a blank
        if self.grid[row][col] > 0:
            return self.solve(self.grid, row, col + 1)

        
        for n in range(1, 10):

            # check if every number fits this square
            if self.isok(self.grid, row, col, n):
                self.grid[row][col] = n

                # start solving the next square
                if self.solve(self.grid, row, col + 1):
                    return True

            self.grid[row][col] = 0
        return False

    # solve using bitmask
    def solve16x16(self, grid, row=0, col=0):
        # if it oversteps the board just stop
        if row == 15 and col == 16:
            return True

        # lead it to the next row if it oversteps columns while checking
        if col == 16:
            row += 1
            col = 0

        # start a tree if there's a blank
        if self.grid[row][col] > 0:
            return self.solve16x16(self.grid, row, col + 1)

        
        for n in range(1, 17):

            # check if every number fits this square
            if self.isok16x16(self.grid, row, col, n):
                self.grid[row][col] = n
                # start solving the next square
                if self.solve16x16(self.grid, row, col + 1):
                    return True

            self.grid[row][col] = 0
        return False

    # solve using bitmask
    def solve4x4(self, grid, row=0, col=0):
        # if it oversteps the board just stop
        if row == 3 and col == 4:
            return True

        # lead it to the next row if it oversteps columns while checking
        if col == 4:
            row += 1
            col = 0

        # start a tree if there's a blank
        if self.grid[row][col] > 0:
            return self.solve4x4(self.grid, row, col + 1)

        
        for n in range(1, 5):

            # check if every number fits this square
            if self.isok4x4(self.grid, row, col, n):
                self.grid[row][col] = n
                # start solving the next square
                if self.solve4x4(self.grid, row, col + 1):
                    return True

            self.grid[row][col] = 0
        return False
    
    def start_solve(self):
        return self.solve(self.grid)

    def start_solve16x16(self):
        return self.solve16x16(self.grid)

    def start_solve4x4(self):
        return self.solve4x4(self.grid)

    
    

