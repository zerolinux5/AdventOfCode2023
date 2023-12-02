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
    start = 0
    end = 0
    current = ''
    if forward:
        translationMap = translationMapForward
    else:
        translationMap = translationMapBackward
    posibilities = set(translationMap.keys())
    while end < len(line):
        if line[end].isdigit():
            return line[end]
        current += line[end]
        removeSet = set()
        for posibility in posibilities:
            if posibility.startswith(current):
                continue
            else:
                removeSet.add(posibility)
        posibilities -= removeSet
        if len(posibilities) == 1 and current in posibilities:
            return str(translationMap[current])
        elif len(posibilities) == 0:
            start += 1
            end = start
            current = ''
            posibilities = set(translationMap.keys())
        else:
            end += 1

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