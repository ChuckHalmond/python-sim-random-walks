
import sys

sys.path.insert(0, 'src')

from src.io import inputInt, inputFloat, inputChoice, progressBar
from src.commands import testCommand, simulateCommand, plotCommand

def main():
    QUIT = 1

    commandsDict = {
        'T': testCommand,
        'S': simulateCommand,
        'G': plotCommand,
        'Q': QUIT
    }

    while (True):

        choice = inputChoice(
            prompt = 'a command to execute',
            choices = [
                {'value': 'T', 'desc': 'to [T]est the PRNG with the chi 2 method'},
                {'value': 'S', 'desc': 'to execute a random walk [S]imulation'},
                {'value': 'G', 'desc': 'to plot the random walks end-to-end distances [G]raph'},
                {'value': 'Q', 'desc': 'to [Q]uit this program'}
            ],
        )

        command = commandsDict[choice]

        if command == QUIT:
            break

        command()

if __name__== '__main__':

    main()