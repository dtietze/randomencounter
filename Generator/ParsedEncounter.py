import xml.etree.ElementTree as ElementTree
class ParsedEncounter(object):
    """docstring for ParsedEncounter."""

    def __init__(self, treein:ElementTree):
        super(ParsedEncounter, self).__init__()
        self.treein = treein
        self.name = Input.get(Name)
        self.startnumber = Input.get(StartNumber)
        self.endnumber = Input.get(EndNumber)
        self.description = Input.get(Description)
        self.next = Input.get(Next)
    def
