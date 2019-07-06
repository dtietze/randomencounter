import xml.etree.ElementTree as ElementTree

def main():
    readytable = TableSet(ElementTree.parse(input("Enter Filename: ")))
    action = input("Enter ROLL or DONE")
    while input != "DONE":
        if input == "ROLL":
            readytable.makeencounter()
        action = input("Enter ROLL or DONE")

if __name__ == '__main__':
    main()
