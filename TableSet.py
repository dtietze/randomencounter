import xml.etree.ElementTree as ElementTree
from Encounter import Encounter
from Roller import Roller
class TableSet(object):
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
        super(TableSet, self).__init__()
        self.tableslist = list()
        self.start = EncounterTable(treein.find("[@Name=StartHere]"))
        for child in treein:
            tableslist.add(EncounterTable(child))


    def makeencounter():
        """
        Creates an encounter based on existing encoutners and a roller
        """
        nextqueue = Queue.queue()
        expected = list()
        encounterstring = ""
        nextname = ""
        nextqueue.add(self.start)
        while !nextqueue.empty():
            nextname = nextqueue.get()
            for table in self.tableslist:
                if table.getname() == nextname:
                    expected = table.generateencounter()
            if expected.length() > 1:
                nextqueue.put(expected[1])
            encounterstring = encounterstring + expected[0]
        return encounterstring
