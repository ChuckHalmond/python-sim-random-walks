from .prng import PRNG
from .io import FLOAT_FORMATTER
from scipy import stats

class PRNGTest:

    def __init__(self, prng: PRNG):
        self.prng = prng
    
    def generateTwoDiceSumsFromPrng(self, size):
        prngResult = 11 * [0]

        for _ in range(size):
            randSum = (int)(self.prng.nextInRange(1, 7)) + (int)(self.prng.nextInRange(1, 7))
            prngResult[randSum - 2] = prngResult[randSum - 2] + 1

        # combines the results for 2 and 3 and for 11 and 12
        prngResult[1] = prngResult[1] + prngResult[0]
        prngResult[9] = prngResult[9] + prngResult[10]

        prngResult = prngResult[1:10]

        return prngResult

    def generateTwoDiceSumsFromTruth(self, size):
        # proba for getting respectively 2 or 3, 4, 5, 6, 7, 8, 9, 10 and 11 or 12
        truthProba: list(float) = [1/12, 1/12, 1/9, 5/36, 1/6, 5/36, 1/9, 1/12, 1/12]
        
        truthResult: list(int) = 9 * [0]

        for i in range(9):
            truthResult[i] = size * truthProba[i]

        return truthResult

    def testChi2OnTwoDiceSum(self, setSize):

        print(30 * '=')
        print('Chi 2 Test | Two Dice Sum')
        print(30 * '=')

        print(10 * '-')
        print('Input')
        print(10 * '-')

        print('Set size = ' + str(setSize))

        prngResults = self.generateTwoDiceSumsFromPrng(setSize)
        truthResults = self.generateTwoDiceSumsFromTruth(setSize)

        print(8 * '-')
        print('Output')
        print(8 * '-')

        khi2Df8 = 15.51
        print('khi2Df8 = ' + str(khi2Df8))

        print('• Expected two dice sums distribution : ' + str([FLOAT_FORMATTER.format(truthResult) for truthResult in truthResults]).replace('\'', ''))
        print('• Actual distribution : ' + str([FLOAT_FORMATTER.format(prngResult) for prngResult in prngResults]).replace('\'', ''))

        T = sum(
            [pow(prngResults[i] - truthResults[i], 2) / truthResults[i] for i in range(len(prngResults))]
        )
        
        stats.chisquare(prngResults, truthResults)[1]

        print('• Value of the test : ' + str(FLOAT_FORMATTER.format(T)))
        if (T < khi2Df8):
            print(str(FLOAT_FORMATTER.format(T)) + ' < ' + str(FLOAT_FORMATTER.format(khi2Df8)))
            print('=> Data seems to follow an uniform distribution')
        else:
            print(str(FLOAT_FORMATTER.format(T)) + ' >= ' + str(FLOAT_FORMATTER.format(khi2Df8)))
            print('=> Data seems not to follow an uniform distribution')