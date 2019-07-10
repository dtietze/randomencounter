import Roller
import re
class Description(object):
    """
    a class used to hold an encounter description

    ...

    Attributes
    ----------
    descriptionlist : list
        Contains the description, with rollable parts separated. Pattern goes {..., rollable, nonrollable, rollable, ...}
    toroll : list
        contains Rollers for all rollable portions
    rollnumbers: list
        contains indices of rollable portions

    Methods
    -------
    rollDescription()
        Recreates a description with roller input.
    """

    def __init__(self, descriptionstring):
        """
        Parameters
        ----------
        description : string
            full description as a string, with rollable sections denoted by @xdy@
        """
        super(Description, self).__init__()
        pattern = re.compile("\d*d\d*")
        self.descriptionlist = str(descriptionstring).split("@")
        self.toroll = list()
        self.rollnumbers = list()
        k = 0
        while k < len(self.descriptionlist):
            if (self.descriptionlist[k]):
                if (re.fullmatch(pattern,self.descriptionlist[k])):
                    self.toroll.append((Roller.stringtoroller(self, self.descriptionlist[k])))
                    self.rollnumbers.append(k)
            k = k + 1

    def rolldescription(self):
        """
        outputs a fully rolled encounter description.

        Returns
        -------
        outstring : string
            the string with a combination of the words and rolls
        """
        i = 0
        j = 0
        outstring = ""
        while i < len(self.descriptionlist):
            if i in self.rollnumbers:
                outstring = outstring + str(self.toroll[j].roll())
                j = j + 1
            else:
                outstring = outstring + self.descriptionlist[i]
            i = i + 1
        return outstring
