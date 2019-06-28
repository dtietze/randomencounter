import xml.etree.ElementTree as ElementTree
class ParsedTable(object):
    """docstring for ParsedTable."""

    def __init__(self, Input:ElementTree):
        super(ParsedTable, self).__init__()
        self.Input = Input
        self.ParsedEncouters = set()
        for child in self.Input
            ParsedEncouters.add(ParsedEncounter(child))
