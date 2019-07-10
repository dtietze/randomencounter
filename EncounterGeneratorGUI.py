from TableSet import TableSet
from xml.etree import ElementTree
import tkinter

class EncounterGeneratorGUI(object):
    """docstring for EncounterGeneratorGUI."""

    def __init__(self, master):
        super(EncounterGeneratorGUI, self).__init__()
        self.win = master
        self.tree = ElementTree.parse(input("Enter filename: "))
        self.root = self.tree.getroot()
        self.outstring = ""
        self.readytable = TableSet(self.root)
        self.win.title("Random Encounter")
        self.but = tkinter.Button(self.win, text = 'ROLL', command = self.rollbutton)
        self.but.pack()
        self.tex = tkinter.Text(self.win, wrap = tkinter.WORD)
        self.tex.pack()
        self.tex.configure(state='normal')
        self.tex.insert(tkinter.END, "No Encounter Yet")
        self.tex.configure(state='disabled')

    def rollbutton(self):
        self.outstring = self.readytable.makeencounter()
        self.tex.configure(state='normal')
        self.tex.delete(1.0, tkinter.END)
        self.tex.insert(tkinter.END, self.outstring)
        self.tex.configure(state='disabled')
