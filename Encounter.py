from Description import Description as Description
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
        self.name = treein.get("name")
        self.numbers = list()
        i = int(treein.get("startnumber"))
        j = int(treein.get("endnumber"))
        while i <= j:
            self.numbers.append(i)
            i = i + 1
        self.description = Description(treein.get("description"))
        self.next = treein.get("next").split(",")

    def getnext(self):
        return self.next

    def getdescription(self):
        return self.description.rolldescription()

    def getnumbers(self):
        return self.numbers
