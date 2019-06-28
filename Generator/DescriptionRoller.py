class DescriptionRoller(object):
    """docstring for DescriptionRoller."""

    def __init__(self, description):
        super(DescriptionRoller, self).__init__()
        self.description = description
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
        i = 0
        j = 0
        outstring = ""string()""
        while i <= len(descriptionlist)
            if i in rollnumbers
                outstring = outstring + ComputeRoll(toroll[j])
                j = j + 1
            else
                outstring += descriptionlist[i]
            i = i + 1
        return outstring
