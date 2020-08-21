'''
    Utilities related to Directions
'''
from enum import Enum
from math import sqrt

class Direction(Enum):
    right = 1
    left = 2
    top = 3
    bottom = 4

def getRandomDirection(prng, directions):
    return directions[(int)(prng.nextInRange(0, len(directions)))]

def directionToVector(direction):
    if (direction == Direction.right):
        return [1, 0]
    elif (direction == Direction.left):
        return [-1, 0]
    elif (direction == Direction.top):
        return [0, 1]
    elif (direction == Direction.bottom):
        return [0, -1]

def directionToArrowSymbol(direction):
    if (direction == Direction.right):
        return '→'
    elif (direction == Direction.left):
        return '←'
    elif (direction == Direction.top):
        return '↑'
    elif (direction == Direction.bottom):
        return '↓'

def twoLastDirectionsToPathSymbol(previousDirection, currentDirection):

    if (previousDirection == Direction.right):
        if (currentDirection == Direction.right or currentDirection == Direction.left):
            return '─'
        elif (currentDirection == Direction.top):
            return '┘'
        elif (currentDirection == Direction.bottom):
            return '┐'

    elif (previousDirection == Direction.left):
        if (currentDirection == Direction.right or currentDirection == Direction.left):
            return '─'
        elif (currentDirection == Direction.top):
            return '└'
        elif (currentDirection == Direction.bottom):
            return '┌'

    elif (previousDirection == Direction.top):
        if (currentDirection == Direction.right):
            return '┌'
        elif (currentDirection == Direction.left):
            return '┐'
        elif (currentDirection == Direction.top or currentDirection == Direction.bottom):
            return '│'

    elif (previousDirection == Direction.bottom):
        if (currentDirection == Direction.right):
            return '└'
        elif (currentDirection == Direction.left):
            return '┘'
        elif (currentDirection == Direction.top or currentDirection == Direction.bottom):
            return '│'

def combinePathSymbols(previousSymbol, currentSymbol):

    if (previousSymbol == 'D'):
        return 'D'
    if (currentSymbol == 'A'):
        return 'A'
    elif (previousSymbol == ' ' or previousSymbol == currentSymbol):
        return currentSymbol

    # straight lines

    if (currentSymbol == '─'):
        if (previousSymbol == '┐' or previousSymbol == '┌' or previousSymbol == '┬'):
            return '┬'
        elif (previousSymbol == '└' or previousSymbol == '┘' or previousSymbol == '┴'):
            return '┴'

    if (currentSymbol == '│'):
        if (previousSymbol == '┐' or previousSymbol == '┘' or previousSymbol == '┤'):
            return '┤'
        elif (previousSymbol == '└' or previousSymbol == '┌' or previousSymbol == '├'):
            return '├'

    # angles

    if (currentSymbol == '┐'):
        if (previousSymbol == '│' or previousSymbol == '┘' or previousSymbol == '┤'):
            return '┤'
        elif (previousSymbol == '─' or previousSymbol == '┌' or previousSymbol == '┬'):
            return '┬'

    if (currentSymbol == '┌'):
        if (previousSymbol == '│' or previousSymbol == '└' or previousSymbol == '├'):
            return '├'
        elif (previousSymbol == '─' or previousSymbol == '┐' or previousSymbol == '┬'):
            return '┬'

    if (currentSymbol == '└'):
        if (previousSymbol == '│' or previousSymbol == '┌' or previousSymbol == '├'):
            return '├'
        elif (previousSymbol == '─' or previousSymbol == '┘' or previousSymbol == '┴'):
            return '┴'

    if (currentSymbol == '┘'):
        if (previousSymbol == '│' or previousSymbol == '┐' or previousSymbol == '┤'):
            return '┤'
        elif (previousSymbol == '─' or previousSymbol == '└' or previousSymbol == '┴'):
            return '┴'
    
    # crossed angles

    if (currentSymbol == '├'):
        if (previousSymbol == '│' or previousSymbol == '┌' or previousSymbol == '└'):
            return '├'

    if (currentSymbol == '┤'):
        if (previousSymbol == '│' or previousSymbol == '┐' or previousSymbol == '┘'):
            return '┤'

    if (currentSymbol == '┬'):
        if (previousSymbol == '─' or previousSymbol == '┐' or previousSymbol == '┌'):
            return '┬'

    if (currentSymbol == '┴'):
        if (previousSymbol == '─' or previousSymbol == '┘' or previousSymbol == '└'):
            return '┴'

    return '┼'

def oppositeDirection(direction):
    if (direction == Direction.right):
        return Direction.left
    elif (direction == Direction.left):
        return Direction.right
    elif (direction == Direction.top):
        return Direction.bottom
    elif (direction == Direction.bottom):
        return Direction.top

def sumVectors(vectorA, vectorB):
    return [a + b for a, b in zip(vectorA, vectorB)]
    
def diffVectors(vectorA, vectorB):
    return [a - b for a, b in zip(vectorA, vectorB)]

def getMinXOfVectors(vectors):
    return min(vectors, key = lambda val : val[0])[0]

def getMaxXOfVectors(vectors):
    return max(vectors, key = lambda val : val[0])[0]

def getMinYOfVectors(vectors):
    return min(vectors, key = lambda val : val[1])[1]

def getMaxYOfVectors(vectors):
    return max(vectors, key = lambda val : val[1])[1]

def squared2DVecDist(dep, dest):
    return pow(dest[0] - dep[0], 2) + pow(dest[1] - dep[1], 2)