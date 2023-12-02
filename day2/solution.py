def parseLine(line):
    gameName, gamesPlayed = line.split(':')
    gameId = gameName.split(' ')[1]
    games = gamesPlayed.split(';')
    return gameId, games

def parseGame(game):
    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    colors = game.split(',')
    for color in colors:
        color = color.strip()
        number, colorName = color.split(' ')
        if int(number) > limits[colorName]:
            return False
    return True

def soln1(data):
    sum = 0
    for line in data:
        line = line.lower().strip()
        gameid, games = parseLine(line)
        is_valid = True
        for game in games:
            if not parseGame(game):
                is_valid = False
                break
        if is_valid:
            sum += int(gameid)
    return sum

def getMinColorCountFromGame(game):
    limits = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    colors = game.split(',')
    for color in colors:
        color = color.strip()
        number, colorName = color.split(' ')
        limits[colorName] = max(limits[colorName], int(number))
    return limits

def soln2(data):
    sum = 0
    for line in data:
        line = line.lower().strip()
        games = line.split(':')[1].split(';')
        actualLimits = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for game in games:
            gameLimits = getMinColorCountFromGame(game)
            for color in actualLimits:
                actualLimits[color] = max(actualLimits[color], gameLimits[color])
        runningSum = 1
        for color in actualLimits:
            runningSum *= actualLimits[color]
        sum += runningSum
    return sum

with open('input.txt') as f:
    data = f.readlines()
    print(soln2(data))