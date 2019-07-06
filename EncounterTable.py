class EncounterTable(object):
    """
    a class used to hold an encounter as its pieces

    ...

    Attributes
    ----------
    name : string
        name of encounter
    startnumber : int
        first rolled number of encoutner
    endnumber : int
        number on table where the encounter ends
    description : string
        description of encounter
    next : list
        list of next encounters
    """
    def __init__(self, treein:ElementTree):
        """
        Parameters
        ----------
        treein : elementtree
            tree contianing pieces which will be portioned out
        """
        super(EncounterTable, self).__init__()
        self.name = Input.get(Name)
        self.dice = Roller.stringtoroller(treein.get(Dice))
        self.description = DescriptionRoller(Input.get(Description))
        self.encounterlist = list()
        for child in treein:
            encounterlist.add(Encounter(child))

    def getname(self):
        return self.name

    def generateencounter(self):
        
