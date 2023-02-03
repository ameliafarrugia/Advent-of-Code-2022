scores = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
wins = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
draws = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]

def fileInput(fileName):
	arr = []
	with open(fileName) as f:
		for line in f:
			line = line.rstrip('\n')
			line = line.split()
			arr.append(line)
	return arr

def dayTwoPartOne(fileName):
	arr = fileInput(fileName)
	score = 0
	for x in range(len(arr)):
		round = arr[x]
		if round in wins:
			score += 6
		if round in draws:
			score += 3
		score += scores[round[1]]
	return score

def dayTwoPartTwo(fileName):
	arr = fileInput(fileName)
	score = 0 
	for x in range(len(arr)):
		round = arr[x]
		result = round[1]
		opponent = round[0]
		if result == 'X':
			if opponent == 'A':
				score += 3
			if opponent == 'B':
				score += 1
			if opponent == 'C':
				score += 2
		elif result == 'Y':
			score += 3
			score += scores[opponent]
		else:
			score += 6
			if opponent == 'A':
				score += 2
			if opponent == 'B':
				score += 3
			if opponent == 'C':
				score += 1
	return score
