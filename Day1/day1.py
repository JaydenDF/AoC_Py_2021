count = 1
answer = 0
intList = []
with open('day1PuzzleInput1') as file:
    lines = [line.rstrip('\n') for line in file]
    for line in lines:
        intLine = int(line)
        intList.append(intLine)
    for number in intList:
        if intList[count] > number:
            answer += 1
        if count < 1999:
            count += 1
file.close()

print(answer)
