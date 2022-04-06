count = 1
count1 = 0  # added for part 2 ------
count2 = 1  # added for part 2 ------
count3 = 2  # added for part 2 ------
count4 = 1   # added for part 2 ------
answer = 0
answer2 = 0  # added for part 2 ------
intList = []
sumList = []  # added for part 2 ------
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
    # part 2 ------
    for counter in intList:
        sum1 = intList[count1] + intList[count2] + intList[count3]
        sumList.append(sum1)
        if count3 < 1999:
            count1 += 1
            count2 += 1
            count3 += 1
    for sum2 in sumList:
        if sumList[count4] > sum2:
            answer2 += 1
        if count4 < 1999:
            count4 += 1

print(answer)
print(answer2)  # added for part 2 ------

file.close()
