import DescriptionRoller
import xml.etree.ElementTree as ElementTree
class Encounter(object):
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
        super(Encounter, self).__init__()
        self.name = treein.get(Name)
        self.numbers = list()
        i = treein.get(StartNumber)
        while i <= treein.get(EndNumber):
            numbers.add(i)
            i = i + 1
        self.description = Description(treein.get(Description))
        self.next = treein.get(Next)

    def getnext(self):
        return self.next

    def getdescription(self):
        return self.description.rolldescription()
