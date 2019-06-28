import xml.etree.ElementTree as ElementTree
class EncounterTablesInput(object):
    """docstring for EncounterTablesInput."""

    def __init__(self, FileName:String):
        super(EncounterTablesInput, self).__init__()
        self.FileName = FileName
        self.EncounterTables = ElementTree.parse(FileName)
