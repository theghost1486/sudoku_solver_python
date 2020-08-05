import numpy as np

sudoku = [[7,2,0,8,0,0,0,0,4],
		  [0,5,0,7,0,0,0,0,6],
		  [3,0,9,2,6,0,0,0,0],
		  [0,0,0,4,0,0,7,9,3],
		  [9,3,0,1,7,0,0,0,2],
		  [4,0,2,9,0,6,0,0,1],
		  [0,1,0,6,2,9,0,0,5],
		  [0,9,4,0,0,7,2,6,0],
		  [2,0,0,0,8,4,0,7,9]]





def possible(y,x,n):
	global sudoku 
	for i in range(0,9):
		if sudoku[y][i] == n:
			return  False
		if sudoku[i][x] == n:
			return False
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if sudoku[y0+i][x0+i] == n:
				return False
	return True


def solver():
	global sudoku
	for y in range(9):
		for x in range(9):
			if sudoku[y][x]==0:
				for n in range(1,10):
					if possible(y,x,n):
						sudoku[y][x]=n
						solver()
						sudoku[y][x]=0
				return
	print(np.matrix(sudoku))
	input("More?")


solver()