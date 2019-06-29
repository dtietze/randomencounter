import xml.etree.ElementTree as ElementTree
class EncounterTablesInput(object):
    """
    Inputs the encounter tables as an element tree

    ...

    Attributes
    ----------
    encountertables : elementtee
        Elment tree of all encounter tables

    """

    def __init__(self, filename:String):
        """
        Parameters
        ----------
        filename : string
            specifies file to be parsed
        """
        super(EncounterTablesInput, self).__init__()
        self.encountertables = ElementTree.parse(filename)
