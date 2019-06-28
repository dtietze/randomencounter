import xml.etree.ElementTree as ElementTree
class ParsedTable(object):
    """docstring for ParsedTable."""

    def __init__(self, treein:ElementTree):
        super(ParsedTable, self).__init__()
        self.treein = treein
        self.parsedencounters = set()
        for child in self.treein
            ParsedEncouters.add(ParsedEncounter(child))
