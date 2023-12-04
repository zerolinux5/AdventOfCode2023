def soln1(lines):
    sum = 0
    for line in lines:
        line = line.lower().strip()
        _, cardInfo = line.split(':')
        winningNumberCard, myNumberCard = cardInfo.split('|')
        winningNumbers = set(winningNumberCard.split())
        myNumbers = myNumberCard.split()
        runningSum = 0
        for number in myNumbers:
            if number in winningNumbers:
                if runningSum == 0:
                    runningSum = 1
                else:
                    runningSum *= 2
        sum += runningSum
    return sum

with open('input.txt') as f:
    lines = f.readlines()
    print(soln1(lines))