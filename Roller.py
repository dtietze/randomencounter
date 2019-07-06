import random
class Roller(object):
    """
    A class used to roll a set of dice multiple times

    ...

    Attributes
    ----------
    n : int
        represents the number of dice, pulled from nd
    d : int
        represents the size of dice, pulled from nd

    Methods
    -------
    Roll()
        randomizes a number based on the roller's dice
    """

    def __init__(self, nd):
        """
        Parameters
        ----------
        nd : tuple
            represents (number of dice, size of dice)
        """
        super(Roller, self).__init__()
        self.n = nd[0]
        self.d = nd[1]

    def roll(self):
        """
            randomizes a number based on the roller's dice

            Returns
            -------
            total : int
                the total of the rolls
        """
        i = 0
        total = 0
        while i < self.n:
            total = total + random.randint(1,self.d)
            i = i + 1
        return total

def stringtoroller(self, stringroller):
    """
    Creates a roller based on a string

    Returns
    ---------------
    newroller: Roller
    """
    return Roller(tuple(stringroller.split(d)))
    
