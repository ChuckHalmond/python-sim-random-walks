from .utils import *
from .prng import PRNG

class RandomWalk():

    def __init__(self, prng: PRNG):
        self.prng = prng
        self.position = [0, 0]
        self.direction = None
        self.pathDirections = []
        self.pathPositions = [self.position]

    def resetPath(self):
        self.position = [0, 0]
        self.direction = None
        self.pathDirections = []
        self.pathPositions = [self.position]

    def runSteps(self, steps):
        '''
        Must be implemented!
        '''
        return
    
    def squaredPathDist(self):
        if (len(self.pathPositions) < 2):
            return 0
        else:
            return squared2DVecDist(
                self.pathPositions[0],
                self.pathPositions[len(self.pathPositions) - 1]
            )

    
    def displayState(self):

        print('[' + self.__class__.__name__ + ']')

        # print the number of steps

        print('-Steps')
        print(str(len(self.pathDirections)))

        # prints the directions the path is following
        
        print('-Directions')
        for direction in self.pathDirections:
            print(directionToArrowSymbol(direction), end=' ')
        print()

        # determines the path's symbols from the directions

        pathSymbols = ['D']
        for i in range(len(self.pathDirections) - 1):
            pathSymbols.append(twoLastDirectionsToPathSymbol(self.pathDirections[i], self.pathDirections[i + 1]))
        pathSymbols.append('A')

        # builds the path matrix with placeholders

        # computes some interesting values 
        pathWidth = getMaxXOfVectors(self.pathPositions) - getMinXOfVectors(self.pathPositions) + 1
        pathHeight = getMaxYOfVectors(self.pathPositions) - getMinYOfVectors(self.pathPositions) + 1
        pathTopLeftMargin = [getMinXOfVectors(self.pathPositions), getMinYOfVectors(self.pathPositions)]

        pathMatrix = []
        for y in range(pathHeight):
            pathRow = []
            for x in range(pathWidth):
                pathRow.append(' ')
            pathMatrix.append(pathRow)

        # fills the path matrix with the right symbols
        
        for i, pathPosition in enumerate(self.pathPositions):
            # translates the current position
            [positionX, positionY] = diffVectors(pathPosition, pathTopLeftMargin)
            # combines the previous and the current symbol at the current position
            pathMatrix[positionY][positionX] = combinePathSymbols(pathMatrix[positionY][positionX], pathSymbols[i])

        # prints the path matrix

        print('-Path')
        for y in reversed(range(pathHeight)):
            for x in range(pathWidth):
                print(pathMatrix[y][x], end='')
            print()

class SimpleRandomWalk(RandomWalk):

    def runSteps(self, steps):
        for _ in range(steps):

            self.direction = getRandomDirection(self.prng, list(Direction))
            self.position = sumVectors(self.position, directionToVector(self.direction))

            self.pathDirections.append(self.direction)
            self.pathPositions.append(self.position)

class NonReversingWalk(RandomWalk):

    def runSteps(self, steps):

        for _ in range(steps):
            
            availableDirections = list(Direction)
            if (self.direction != None):
                availableDirections.remove(oppositeDirection(self.direction))

            self.direction = getRandomDirection(self.prng, availableDirections)
            self.position = sumVectors(self.position, directionToVector(self.direction))

            self.pathDirections.append(self.direction)
            self.pathPositions.append(self.position)

class SelfAvoidingWalk(RandomWalk):
    
    def runSteps(self, steps):

        for _ in range(steps):

            availableDirections = list(Direction)

            for availableDirection in list(Direction):
                testPosition = sumVectors(self.position, directionToVector(availableDirection))

                if (self.pathPositions.__contains__(testPosition)):
                    availableDirections.remove(availableDirection)

            if (len(availableDirections) == 0):
                return

            self.direction = getRandomDirection(self.prng, availableDirections)
            self.position = sumVectors(self.position, directionToVector(self.direction))

            self.pathDirections.append(self.direction)
            self.pathPositions.append(self.position)