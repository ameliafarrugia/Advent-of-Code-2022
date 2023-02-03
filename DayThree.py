def fileInput(fileName):
	arr = []
	with open(fileName) as f:
		for line in f:
			line = line.rstrip('\n')
			firstHalf = line[:int(len(line)/2)]
			secondHalf = line[int(len(line)/2):]
			line = [firstHalf, secondHalf]
			arr.append(line)
	return arr

def priorityMap():
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	map = {}
	for i in range(len(alphabet)):
		map[alphabet[i:i+1]] = i + 1
		map[alphabet[i:i+1].capitalize()] = i+27
	return map 

def findRepeatChars(rucksacks):
	repeats = []
	for compartments in rucksacks:
		i = 0
		while not compartments[0][i:i+1] in compartments[1]:
			i+=1
		repeats.append(compartments[0][i:i+1])
	return repeats 

def totalSum(repeats, priorities):
	sum = 0
	for repeat in repeats:
		sum += priorities[repeat]
	return sum 

def inAllThree(rucksacks):
	repeats = []
	for i in range(0, len(rucksacks), 3):
		rucksackOne = rucksacks[i][0] + rucksacks[i][1]
		rucksackTwo = rucksacks[i+1][0] + rucksacks[i+1][1]
		rucksackThree = rucksacks[i+2][0] + rucksacks[i+2][1]
		j = 0
		while not (rucksackOne[j:j+1] in rucksackTwo and rucksackOne[j:j+1] in rucksackThree):
			j += 1
		repeats.append(rucksackOne[j:j+1])
	return repeats 

def dayThreePartOne(fileName):
	arr = fileInput(fileName)
	repeats = findRepeatChars(arr)
	priorities = priorityMap()
	return totalSum(repeats, priorities)

def dayThreePartTwo(fileName):
	arr = fileInput(fileName)
	repeats = inAllThree(arr)
	priorities = priorityMap()
	return totalSum(repeats, priorities)


