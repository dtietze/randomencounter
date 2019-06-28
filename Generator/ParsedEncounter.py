import xml.etree.ElementTree as ElementTree
class ParsedEncounter(object):
    """docstring for ParsedEncounter."""

    def __init__(self, Input:ElementTree):
        super(ParsedEncounter, self).__init__()
        self.Input = Input
        self.Name = Input.get(Name)
        self.StartNumber = Input.get(StartNumber)
        self.EndNumber = Input.get(EndNumber)
        self.Description = Input.get(Description)
        self.Next = Input.get(Next)
