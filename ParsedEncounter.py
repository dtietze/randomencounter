import xml.etree.ElementTree as ElementTree
class ParsedEncounter(object):
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
    Methods
    -------
    rollDescription()
        Recreates a description with roller input.
    """
    def __init__(self, treein:ElementTree):
        """
        Parameters
        ----------
        treein : elementtree
            tree contianing pieces which will be portioned out
        """
        super(ParsedEncounter, self).__init__()
        self.name = Input.get(Name)
        self.startnumber = Input.get(StartNumber)
        self.endnumber = Input.get(EndNumber)
        self.description = Input.get(Description)
        self.next = Input.get(Next)
