from queue import Queue as Queue
from EncounterTable import EncounterTable
from Roller import Roller
import xml.etree.ElementTree as ElementTree
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
    def __init__(self, treein):
        """
        Parameters
        ----------
        treein : elementtree
            tree contianing pieces which will be portioned out
        """
        super(TableSet, self).__init__()
        self.tableslist = list()
        for child in treein:
            self.tableslist.append(EncounterTable(child))
        for thing in self.tableslist:
            if thing.getname() == "StartHere":
                self.start = thing

    def makeencounter(self):
        """
        Creates an encounter based on existing encoutners and a roller
        """
        nextqueue = Queue()
        expected = list()
        encounterstring = ""
        nextname = ""
        nextqueue.put(self.start)
        while nextqueue.empty() == False:
            nextname = nextqueue.get().getname()
            for table in self.tableslist:
                if table.getname() == nextname:
                    expected = table.generateencounter()
            if len(expected) > 1:
                for table in self.tableslist:
                    i = 0
                    while i < len(expected[1]):
                        if table.getname() == expected[1][i]:
                            nextqueue.put(table)
                        i = i + 1
            encounterstring = encounterstring + expected[0] + "\n"
        return encounterstring
