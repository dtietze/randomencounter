import Roller
class DescriptionRoller(object):
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

    def __init__(self, description):
        """
        Parameters
        ----------
        description : string
            full description as a string, with rollable sections denoted by @xdy@
        """
        super(DescriptionRoller, self).__init__()
        self.descriptionlist = description.split(@)
        self.toroll = list()
        self.rollnumbers = list()
        k = 0
        while k < len(descriptionlist):
            if descriptionlist[k][1].isdigit():
                nd = tuple(descriptionlist[k].split(d))
                toroll.append((Roller(nd))
                rollnumbers.append(k)
            k = k + 1

    def rollDescription(self):
        """
        outputs a fully rolled encounter description.

        Returns
        -------
        total : int
            the total of the rolls
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
