import Roller
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
        self.descriptionlist = descriptionstring.split(@)
        self.toroll = list()
        self.rollnumbers = list()
        k = 0
        while k < len(descriptionlist):
            if (descriptionlist[k][1].isdigit()):
                toroll.append((Roller.stringtoroller(self, descriptionlist[k])))
                rollnumbers.append(k)
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
        outstring = string()
        while i <= len(descriptionlist):
            if i in rollnumbers:
                outstring = outstring + toroll[j].roll()
                j = j + 1
            else:
                outstring = outstring + descriptionlist[i]
            i = i + 1
        return outstring
