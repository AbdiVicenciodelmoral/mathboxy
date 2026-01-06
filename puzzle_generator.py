import random

class PuzzleGenerator():
    def __init__(self, n: int = 9):
        super().__init__()
        self.n = n
        self.sol = [[]]

    def list_shuffle(self):
      # create lists of shuffled numbers: Fish Yates / Knuth Algorithm
      row_idx, col_idx, map_idx = [[i for i in range(0, self.n)] for _ in range(3)]
      for i in range(self.n-1, 0, -1):
        #Shuffled List for Row Permutation
        row_pos = random.randint(0, i)
        row_idx[i], row_idx[row_pos] = row_idx[row_pos], row_idx[i]

        #Shuffled List for Column permutation
        col_pos = random.randint(0, i)
        col_idx[i], col_idx[col_pos] = col_idx[col_pos], col_idx[i]

        #Shuffled List for Relabeling Numbers
        map_pos = random.randint(0,i)
        map_idx[i], map_idx[map_pos] = map_idx[map_pos], map_idx[i]




      return row_idx,col_idx,map_idx

    def generate_solution(self):
        latin_old = [[0] * self.n for _ in range(self.n)]
        latin_row_perm = [[0] * self.n for _ in range(self.n)]
        latin_col_perm = [[0] * self.n for _ in range(self.n)]
        row_idx, col_idx, map_idx = self.list_shuffle()
        #Latin Square creation
        for r in range(self.n):
           for c in range(self.n):
              latin_old[r][c] = ((r + c) % self.n) + 1
        #Latin Square Row Permutation
        for i in range(self.n):
           orig_row = latin_old[i]
           new_row_num = row_idx[i]
           latin_row_perm[new_row_num] = orig_row
        #Latin Square Col Permutation
        for i in range(self.n):
           temp_row = [0 for _ in range(self.n)]
           print(latin_col_perm)
           for j in range(self.n):
              new_idx = col_idx[j]
              orig_num = latin_row_perm[i][j]
              temp_row[new_idx] = orig_num

           latin_col_perm[i] = temp_row

        self.sol = latin_col_perm

        print("Pre Shuffled Latin Square:")
        print(latin_old)

        print("Post Shuffled Latin Square:")
        print(latin_row_perm)

          
    def uniqueness(self,grid):
        grid_dict ={}
        for i in range(self.n):
           for j in range(self.n):
              num = grid[i][j]
              key = "col "+str(j)+":"+str(num)
              if key in grid_dict:
                 print("Duplicate!")
                 return
              else:
                 grid_dict[key] = True
                 
    def grouping(self):
       tot = self.n**2
       print((tot/3)/2)
      

   
   
   
   
              
                 







        

        
                

                








"""1) PuzzleGenerator

Pure logic. No PyQt imports.

generate_solution(n) -> grid

generate_cages(solution_grid) -> cages

assign_ops_and_targets(solution_grid, cages) -> cages_with_meta

make_puzzle(solution_grid, cages_with_meta) -> puzzle_data

Tip: Represent grids as list[list[int]] and cages as a list of objects/dicts like:

cells: list[(r,c)]

op: "+", "-", "×", "÷", ""

target: int"""