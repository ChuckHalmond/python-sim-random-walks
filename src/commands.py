import time
import simpy
import matplotlib.pyplot as plt

from .io import inputInt, inputFloat, inputChoice, progressBar
from .prng import PRNG
from .prngTest import PRNGTest

from .randomWalks import RandomWalk, SimpleRandomWalk, NonReversingWalk, SelfAvoidingWalk

def testCommand():

    setSize = inputInt(
        prompt = 'the size of the set for the chi 2 test',
        defaultValue = 1000
    )

    testPrng(setSize)

def simulateCommand():

    steps = inputInt(
        prompt = 'the number of steps for the walk',
        defaultValue = 100
    )

    walksDict = {
        'S': SimpleRandomWalk,
        'N': NonReversingWalk,
        'A': SelfAvoidingWalk
    }

    walkChoice = inputChoice(
        prompt = 'a walk to simulate',
        choices = [
            {'value': 'S', 'desc': 'for a [S]imple random walk'},
            {'value': 'N', 'desc': 'for a [N]on-reversing walk'},
            {'value': 'A', 'desc': 'for a self-[A]voiding walk'}
        ]
    )

    delay = inputFloat(
        prompt = 'the delay between each steps (animation)',
        defaultValue = 0.25
    )

    walk = walksDict[walkChoice](PRNG())

    simulateWalkSteps(walk, steps, delay)

def plotCommand():
    maxSteps = inputInt(
        prompt = 'the number of max steps for the walks',
        defaultValue = 50
    )

    iterations = inputInt(
        prompt = 'the size of the set of walks to simulate',
        defaultValue = 100
    )

    plotWalksDistanceGraph(maxSteps, iterations)

def testPrng(setSize):
    
    prng = PRNG()
    prngTest = PRNGTest(prng)
    prngTest.testChi2OnTwoDiceSum(setSize)

def simulateWalkSteps(walk, steps, delay):

    for _ in range(steps):
        walk.runSteps(1)
        walk.displayState()
        time.sleep(delay)

def plotWalksDistanceGraph(maxSteps, iterations):

    walks = [SimpleRandomWalk(PRNG()), NonReversingWalk(PRNG()), SelfAvoidingWalk(PRNG())]

    ax = plt.subplots()[1]

    print('Computing the walks distance graph..')

    # executes the given number of iterations for each walk and each number of steps (from 1 to max)
    # then computes the mean distance for each number of steps
    for walkIdx, walk, in enumerate(walks):
        walkPathDistSum = maxSteps * [0]
        walkPathDistSumCount = maxSteps * [0]

        for it in range(iterations):
            # for each number of steps
            for steps in range(maxSteps):
                walk.runSteps(steps)
                # sums the path distances
                walkPathDistSum[steps] = walkPathDistSum[steps] + walk.squaredPathDist()
                walkPathDistSumCount[steps] = walkPathDistSumCount[steps] + 1
                walk.resetPath()
            
            # updates the progress bar
            progressBar(walkIdx * iterations + it, len(walks) * iterations)
        
        # divides the sum to get the mean distance
        for steps in range(maxSteps):
            walkPathDistSum[steps] = walkPathDistSum[steps] / walkPathDistSumCount[steps]

        # plots the results on the figure
        ax.plot(range(maxSteps), walkPathDistSum, label = walk.__class__.__name__)

    # legends the plot
    ax.set(
        xlabel = 'Number of steps of the walk',
        ylabel = 'End-to-end path distance',
        title = 'End-to-end path distances for the different walks (from ' + str(iterations) + ' iterations)'
    )
    ax.legend(loc='upper left')

    print('\nDone!')

    plt.show()

