def soln1(lines):
    sum = 0
    for line in lines:
        line.strip()
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

with open('input.txt') as f:
    print(soln1(f.readlines()))