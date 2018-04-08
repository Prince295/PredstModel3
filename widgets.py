import tkinter as interface


class ThemedButton(interface.Button):
    def __init__(self, parent = None, **configs):
        interface.Button.__init__(self, parent, **configs)
        self.pack()
        self.config(fg='black', bg = 'white',width = 20,height = 2, font='courier 10', relief='solid', bd=3)

class ThemedMenu(interface.OptionMenu):
    def __init__(self, parent = None, *values, **configs):
        interface.OptionMenu.__init__(self, parent, *values, **configs)
        self.pack
        self.config( fg='black', bg='white', width=10, height=2, font='courier 10', relief='solid', bd=3 )

class Navs(interface.Frame):
    def __init__(self, parent = None, **configs):
        interface.Frame.__init__(self, parent, **configs)
        self.pack(side = "left")
        self.config( bg = 'white', padx = 0, pady = 30)

class Container(interface.Frame):
    def __init__(self, parent = None, **configs):
        interface.Frame.__init__(self, parent, **configs)
        self.pack()
        self.config(bg = 'white', pady = 30)

class ThemedText(interface.Text):
    def __init__(self, parent = None, **configs):
        interface.Text.__init__(self, parent, **configs)
        self.pack(side = "right", expand = True, fill = 'both')
        self.config(bg = '#fce5ff', font = 'verdana 15')

class OutLabel(interface.Label):
    def __init__(self,parent = None, **configs):
        interface.Label.__init__(self, parent, **configs)
        self.pack()
        self.config(fg='black', bg = 'yellow', font = 'verdana 13', relief = 'solid', justify = 'center', width = 15, bd = 1)

class ThemedMessage(interface.Entry):
    def __init__(self, parent = None, **configs):
        interface.Entry.__init__(self, parent, **configs)
        self.pack()
        self.config(bd = 1, fg='black', bg = 'white', font = 'verdana 13', relief='solid', justify = 'center', width = 15, disabledbackground='#fce5ff' , disabledforeground='black')

class CommandButton(interface.Button):
    def __init__(self, parent = None, **configs):
        interface.Button.__init__(self, parent, **configs)
        self.pack()
        self.config(fg = 'black', bg = '#dce6f7', font = 'Times 12', width = 10,  relief = 'solid', justify = 'center', bd = 1, highlightcolor="#37d3ff",
                      highlightbackground="#37d3ff")
