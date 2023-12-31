import copy

def parseNumber(number):
    if number == '':
        return 0
    return int(number)

def insertIntoMap(numberMap, rowIdx, colIdx, numberString):
    number = parseNumber(numberString)
    if number != 0:
        if rowIdx not in numberMap:
            numberMap[rowIdx] = {}
        for i in range(1, len(numberString)+1):
            numberMap[rowIdx][colIdx-i] = number

def generateNumberMapAndSymbolSet(lines, specificChar=None):
    numberMap = {}
    symbolSet = set()
    for rowIdx, line in enumerate(lines):
        row = line.lower().strip()
        numberString = ''
        for colIdx, char in enumerate(row):
            if char.isdigit():
                numberString += char
            elif char == '.':
                insertIntoMap(numberMap, rowIdx, colIdx, numberString)
                numberString = ''
            else:
                insertIntoMap(numberMap, rowIdx, colIdx, numberString)
                numberString = ''
                if specificChar is None or char == specificChar:
                    symbolSet.add(f"{rowIdx},{colIdx}")
        insertIntoMap(numberMap, rowIdx, colIdx, numberString)
    return numberMap, symbolSet

def soln1(lines):
    numberMap, symbolSet = generateNumberMapAndSymbolSet(lines)
    sum = 0
    moveArray = [-1, 0, 1]
    for symbolLocation in symbolSet:
        rowIdx, colIdx = symbolLocation.split(',')
        for rowDelta in moveArray:
            for colDelta in moveArray:
                newRowIdx = int(rowIdx) + rowDelta
                newColIdx = int(colIdx) + colDelta
                if newRowIdx in numberMap and newColIdx in numberMap[newRowIdx]:
                    sum += numberMap[newRowIdx][newColIdx]
                    minColIdx = newColIdx
                    while numberMap[newRowIdx].get(minColIdx) is not None:
                        minColIdx -= 1
                    minColIdx += 1
                    while numberMap[newRowIdx].get(minColIdx) is not None:
                        del numberMap[newRowIdx][minColIdx]
                        minColIdx += 1
                    if numberMap[newRowIdx] == {}:
                        del numberMap[newRowIdx]
    return sum

def soln2(lines):
    numberMap, symbolSet = generateNumberMapAndSymbolSet(lines, '*')
    sum = 0
    moveArray = [-1, 0, 1]
    for symbolLocation in symbolSet:
        rowIdx, colIdx = symbolLocation.split(',')
        numberMapCopy = copy.deepcopy(numberMap)
        count = 0
        runningSum = 1
        for rowDelta in moveArray:
            for colDelta in moveArray:
                newRowIdx = int(rowIdx) + rowDelta
                newColIdx = int(colIdx) + colDelta
                if newRowIdx in numberMapCopy and newColIdx in numberMapCopy[newRowIdx]:
                    count += 1
                    runningSum *= numberMapCopy[newRowIdx][newColIdx]
                    minColIdx = newColIdx
                    while numberMapCopy[newRowIdx].get(minColIdx) is not None:
                        minColIdx -= 1
                    minColIdx += 1
                    while numberMapCopy[newRowIdx].get(minColIdx) is not None:
                        del numberMapCopy[newRowIdx][minColIdx]
                        minColIdx += 1
                    if numberMapCopy[newRowIdx] == {}:
                        del numberMapCopy[newRowIdx]
        if count == 2:
            sum += runningSum
            numberMap = numberMapCopy
    return sum


with open('input.txt') as f:
    lines = f.readlines()
    print(soln2(lines))