class PRNG():
    '''
        A pseudo-random, linear congruential, number generator using the  formula
        > Xi+1 = (aXi + c) mod m\n
        with X0 = `seed`, a = `a`, c = `c` and m = `m`
    '''
    def __init__(self, m: float = pow(2, 64), a: float = 6364136223846793005, c: float = 1442695040888963407, seed: float = 12):
        '''
            Initializes a pseudo-random, linear congruential, number generator using the formula
            > Xi+1 = (aXi + c) mod m\n
            with X0 = `seed`, a = `a`, c = `c` and m = `m`
        '''
        # initialises the density
        self.m = m
        # initialises the multiplier 
        self.a = a
        # initialises the increment
        self.c = c
        # initialises the first random with the seed value
        self.xi = self.seed = seed
        # initialises the counter
        self.i = 0

    def reset(self):
        '''
            Resets the generator to its default `seed` value
        '''
        # restart from the seed
        self.xi = self.seed
        # sets the counter back to 0
        self.i = self.i + 1

    def next(self):
        '''
            Generates the next pseudo-random floating number within the range [0, 1[
        '''
        # computes the next random with the formula Xi+1 = (a * Xi + c) mod m
        self.xi = (self.a * self.xi + self.c) % self.m
        # increments the counter
        self.i = self.i + 1

        # normalizes the density to get a random number in [0, 1)
        normalizedXi = self.xi / self.m

        # returns the result
        return normalizedXi
    
    def nextInRange(self, min: float, max: float):
        '''
            Generates the next pseudo-random floating number within the range [`min`, `max`[
        '''
        # generates the next random and returns it within the given range
        return self.next() * (max - min) + min
