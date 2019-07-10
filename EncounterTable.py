from Encounter import Encounter as Encounter
from Description import Description as Description
from Roller import Roller as Roller
from Roller import stringtoroller as stringtoroller
import xml.etree.ElementTree as ElementTree
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
    def __init__(self, treein):
        """
        Parameters
        ----------
        treein : elementtree
            tree contianing pieces which will be portioned out
        """
        super(EncounterTable, self).__init__()
        self.name = treein.get("name")
        self.dice = Roller(tuple(treein.get("dice").split('d')))
        self.description = Description(treein.get("Description"))
        self.encounterlist = list()
        for child in treein:
            self.encounterlist.append(Encounter(child))

    def getname(self):
        return self.name

    def generateencounter(self):
        thisroll = self.dice.roll()
        expecteddescription = ""
        expectedlist = list()
        expectednext = list()
        for element in self.encounterlist:
            if thisroll in element.getnumbers():
                expecteddescription = expecteddescription + element.getdescription()
                expectednext = element.getnext()
        expectedlist.append(expecteddescription)
        if len(expectednext) > 0:
            expectedlist.append(expectednext)
        return expectedlist
