class DescriptionRoller(object):
    """
    a class used to hold an encounter description

    ...

    Attributes
    ----------
    descriptionlist : list
        a list containing the description, with rollable parts separated.
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
        while k < len(descriptionlist)
            if descriptionlist[k][1].isdigit()
                nd = tuple(descriptionlist[k].split(d))
                toroll.append((ComputeRoll(nd))
                rollnumbers.append(k)
            k = k + 1


    def rollDescription()
        """
            randomizes a number based on the rollers dice

            Returns
            -------
            total : int
                the total of the rolls
        """
        i = 0
        j = 0
        outstring = ""string()""
        while i <= len(descriptionlist)
            if i in rollnumbers
                outstring = outstring + roll(toroll[j])
                j = j + 1
            else
                outstring += descriptionlist[i]
            i = i + 1
        return outstring
