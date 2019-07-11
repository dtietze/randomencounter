from TableSet import TableSet
from xml.etree import ElementTree
import tkinter
from tkinter import ttk

class EncounterGeneratorGUI(object):
    """docstring for EncounterGeneratorGUI."""

    def __init__(self, master):
        super(EncounterGeneratorGUI, self).__init__()
        self.win = master
        self.win.title("Random Encounter")
        self.options = ["Example.xml","OotA2RandomEncounters.xml"]
        self.dro = ttk.Combobox(self.win, values=self.options)
        self.dro.set("Example.xml")
        self.dro.pack()
        self.dro.bind('<<ComboboxSelected>>', self.dmselection)
        self.but = tkinter.Button(self.win, text = 'ROLL', command = self.rollbutton)
        self.but.pack()
        self.tex = tkinter.Text(self.win, wrap = tkinter.WORD)
        self.tex.pack()
        self.tex.configure(state='normal')
        self.tex.insert(tkinter.END, "No Encounter Yet")
        self.tex.configure(state='disabled')
        self.tree = ElementTree.parse("Example.xml")
        self.root = self.tree.getroot()
        self.outstring = ""
        self.readytable = TableSet(self.root)


    def rollbutton(self):
        self.outstring = self.readytable.makeencounter()
        self.tex.configure(state='normal')
        self.tex.delete(1.0, tkinter.END)
        self.tex.insert(tkinter.END, self.outstring)
        self.tex.configure(state='disabled')

    def dmselection(self, event):
        self.tree = ElementTree.parse(self.dro.get())
        self.root = self.tree.getroot()
        self.outstring = ""
        self.readytable = TableSet(self.root)
