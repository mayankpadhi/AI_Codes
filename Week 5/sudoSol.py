import numpy as np
import random

def checkPossible(IPGrid, x, y):
	X0Counter= 0
	Y0Counter= 0
	for i in range(9):
		if x== i:
			continue
		elif IPGrid[i][y]== 0:
			X0Counter+=1

	for j in range(9):
		if y== j:
			continue
		elif IPGrid[x][j]== 0:
			Y0Counter+=1
			
	return max(X0Counter, Y0Counter)

def minRemVal(IPGrid):
	MRVal= [[0 for x in range(9)] for y in range(9)]
	k= 0
	for i in range(9):
		for j in range(9):
			if IPGrid[i][j]!= 0:
				MRVal[i][j]= checkPossible(IPGrid, i, j)

	
	min1= MRVal[0][0]
	minX= 0
	minY= 0
	for i in range(9):
		for j in range(9):
			if min1> MRVal[i][j]:
				min1= MRVal[i][j]
				minX= i
				minY= j

	return (min1, minX, minY)

def sdkConstraints(IPGrid, x, y, myElement):
	flag= 0
	if x< 3 and y< 3:
		for i in range(0, 3):
			for j in range(0, 3):
				if myElement== IPGrid[i][j]:
					return False

	elif x< 3 and (y> 2 and y< 6):
		for i in range(0, 3):
			for j in range(3, 6):
				if myElement== IPGrid[i][j]:
					return False

	elif x< 3 and (y> 5 and y< 9):
		for i in range(0, 3):
			for j in range(6, 9):
				if myElement== IPGrid[i][j]:
					return False

	elif (x> 2 and x< 6) and y< 3:
		for i in range(3, 6):
			for j in range(0, 3):
				if myElement== IPGrid[i][j]:
					return False

	elif (x> 2 and x< 6) and (y> 2 and y< 6):
		for i in range(3, 6):
			for j in range(3, 6):
				if myElement== IPGrid[i][j]:
					return False

	elif (x> 2 and x< 6) and (y> 5 and y< 9):
		for i in range(3, 6):
			for j in range(6, 9):
				if myElement== IPGrid[i][j]:
					return False

	elif (x> 5 and x< 9) and y< 3:
		for i in range(6, 9):
			for j in range(0, 3):
				if myElement== IPGrid[i][j]:
					return False

	elif (x> 5 and x< 9) and (y> 2 and y< 6):
		for i in range(6, 9):
			for j in range(3, 6):
				if myElement== IPGrid[i][j]:
					return False

	elif (x> 5 and x< 9) and (y> 5 and y< 9):
		for i in range(6, 9):
			for j in range(6, 9):
				if myElement== IPGrid[i][j]:
					return False

	for i in range(0, 9):
		if myElement== IPGrid[i][y]:
			return False

	for j in range(0, 9):
		if myElement== IPGrid[x][j]:
			return False
			
	return True

def constraintPropagation(IPGrid, x, y):
	for i in range(0, 9):
		if bool(sdkConstraints(IPGrid, x, y, i)):
			return True

def start():
	print ("Enter the Sudoku Grid(Replace empty positions with 0): ")
	IPGrid = [[0 for x in range(9)] for y in range(9)]
	#IPGrid = [[9, 2, 0, 0, 0, 0, 0, 0, 0], [8, 6, 7, 5, 0, 0, 0, 0, 0], [3, 0, 0, 0, 4, 0, 0, 8, 0], [0, 3, 0, 0, 0, 7, 0, 0, 4], [0, 7, 0, 9, 5, 3, 0, 1, 0], [2, 0, 0, 6, 0, 0, 0, 7, 0], [0, 8, 0, 0, 9, 0, 0, 0, 3], [0, 0, 0, 0, 0, 5, 8, 4, 6], [0, 0, 0, 0, 0, 0, 0, 9, 5]]

	for i in range(9):
		for j in range(9):
			IPGrid[i][j]= input()
	
	trkStack= []												#for dfs implementation
	while(bool(any(0 in sublist for sublist in IPGrid))):
		flag= 0

		rand= random.randint(0, 1)
		if rand== 0:
			min1, minX, minY= minRemVal(IPGrid)							#call MRV
		else:
			minX= random.randint(0, 8)
			minY= random.randint(0, 8)

		for i in range(1, 10):						# keep putting values in 1 box unless satisfied
			if bool(sdkConstraints(IPGrid, minX, minY, i)):		#apply BTS
				IPGrid[minX][minY]= i

				for i in range(9):
					for j in range(9):
						print(str(IPGrid[i][j]), end=" ")
					print()

				print()
				flag= 1
				trkStack.append((i, minX, minY))
				break

		if flag== 0 and len(trkStack)!= 0:
			ind, minX, minY= trkStack.pop()
			IPGrid[minX][minY]

		if flag== 0 and len(trkStack)!= 0:
			ind, minX, minY= trkStack.pop()
			IPGrid[minX][minY]

	for i in range(9):
		for j in range(9):
			print(IPGrid+ "\t")

start()