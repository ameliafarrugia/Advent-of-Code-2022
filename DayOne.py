def fileInput(fileName):
	arr = []
	sum = 0
	with open(fileName) as f:
		for line in f:
			line = line.rstrip('\n')
			if line == '':
				arr.append(sum)
				sum = 0
			else:
				sum += int(line)
		arr.append(sum)
	return arr

def dayOnePartOne(fileName):
	arr = fileInput(fileName)
	arr.sort()
	return max(arr)

def dayOnePartTwo(fileName):
	arr = fileInput(fileName)
	arr.sort()
	return arr[-1] + arr[-2] + arr[-3]
