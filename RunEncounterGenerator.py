from TableSet import TableSet
from xml.etree import ElementTree

def main():
    #filename = input("Enter Filename: ")
    #OotA2RandomEncounters.xml
    #tree = ElementTree.parse(filename)
    tree = ElementTree.parse('OotA2RandomEncounters.xml')
    root = tree.getroot()
    outstring = ""
    readytable = TableSet(root)
    action = input("Enter ROLL or DONE: ")
    while action != "DONE":
        if action == "ROLL":
            outstring = readytable.makeencounter()
            print (outstring)
        action = input("Enter ROLL or DONE: ")
    return 0

if __name__ == '__main__':
    main()
