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

def countNumberOfCopies(winningNumbers, myNumbers):
    count = 0
    for number in myNumbers:
        if number in winningNumbers:
            count += 1
    return count

def soln2(lines):
    cardCount = 0
    cardMapping = {0: 0}
    finalLength = len(lines)
    for idx, line in enumerate(lines):
        if idx in cardMapping:
            cardMapping[idx] += 1
        else:
            cardMapping[idx] = 1
        line = line.lower().strip()
        _, cardInfo = line.split(':')
        winningNumberCard, myNumberCard = cardInfo.split('|')
        winningNumbers = set(winningNumberCard.split())
        myNumbers = myNumberCard.split()
        copyCount = countNumberOfCopies(winningNumbers, myNumbers)
        for i in range(1, copyCount + 1):
            newIdx = idx + i
            if newIdx >= finalLength:
                break
            if newIdx in cardMapping:
                cardMapping[newIdx] += cardMapping[idx]
            else:
                cardMapping[newIdx] = cardMapping[idx]
    cardCount = sum(cardMapping.values())
    return cardCount

with open('input.txt') as f:
    lines = f.readlines()
    print(soln2(lines))