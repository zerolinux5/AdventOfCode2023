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

with open('input.txt') as f:
    data = f.readlines()
    print(soln1(data))