import xml.etree.ElementTree as ElementTree
class EncounterTablesInput(object):
    """docstring for EncounterTablesInput."""

    def __init__(self, filename:String):
        super(EncounterTablesInput, self).__init__()
        self.filename = filename
        self.encountertables = ElementTree.parse(filename)
