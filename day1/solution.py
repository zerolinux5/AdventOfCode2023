def soln1(lines):
    sum = 0
    for line in lines:
        line = line.strip()
        current = ''
        for val in line:
            if val.isdigit():
                current += val
                break
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                current += line[i]
                break
        sum += int(current)
    return sum

def parseLine(line, forward=True):
    translationMapForward = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    translationMapBackward = {
        'eno': 1,
        'owt': 2,
        'eerht': 3,
        'ruof': 4,
        'evif': 5,
        'xis': 6,
        'neves': 7,
        'thgie': 8,
        'enin': 9,
    }
    digit = None
    digitIdx = float("inf")
    for idx, char in enumerate(line):
        if char.isdigit():
            digit = char
            digitIdx = idx
            break
    translationMap = translationMapForward
    if not forward:
        translationMap = translationMapBackward
    for key in translationMap.keys():
        index = line.find(key)
        if index != -1 and index < digitIdx:
            digitIdx = line.index(key)
            digit = str(translationMap[key])
    return digit

def soln2(lines):
    sum = 0
    for line in lines:
        line = line.lower().rstrip()
        parsedLine1 = parseLine(line)
        parsedLine2 = parseLine(line[::-1], False)
        value = parsedLine1 + parsedLine2
        sum += int(value)
    return sum

with open('input.txt') as f:
    data = f.readlines()
    print(soln2(data))