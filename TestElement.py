from xml.etree import ElementTree
tree = ElementTree.parse("OotA2RandomEncounters.xml")
ElementTree.dump(tree)
testlist = list()
testlist.append(tree)
