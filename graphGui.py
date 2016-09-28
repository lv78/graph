#!/usr/bin/env python3
# ToDo : add more comments

import tkinter as tk
import re

class GraphGuiView(tk.Tk) :
  def __init__(self, commands) :
    root = tk.Tk.__init__(self)
    self.CreateWidgets(commands)

  def CreateWidgets(self, commands) : 
    self.CreateMenuBar(commands)
    self.CreateCanvas()

  def CreateMenuBar(self, commands) :
    self.menuBar = GraphMenu(self, commands)
    self.config(menu=self.menuBar)

  def CreateCanvas(self) :
    pass


class GraphMenu(tk.Menu) :
  def __init__(self, parent, commands) :
    tk.Menu.__init__(self, parent, tearoff=0) 
    for label, func in commands :
      if label == "" :
        self.add_separator()
      elif type(func) is list :
        submenu = GraphMenu(self, func)
        self.add_cascade(label=label, menu=submenu)
      else :
        self.add_command(label=label, command=func)
    
class GraphDrawingArea(tk.Canvas) :
  def __init__(self, parent)
    self.width = 500
    self.height = 500
    tk.Canvas.__init__(self, width=self.width, height=self.height)

    
if __name__ == "__main__"  :
  commands=[
    ("File",[
      ("Load", lambda  : print("Load")),
      ("Save", lambda  : print("Save")),
      ("", None),
      ("Quit", lambda : print("Quit"))
    ]),
    ("Edit",[
      ("Add Node", lambda  : print("Add node")),
      ("Add Edge", lambda  : print("Add Edge")),
      ("Tools", [ ("t1", lambda : print("t1")),
                  ("t2", lambda : print("t2"))])
    ]
    )]

  gui = GraphGuiView(commands)
  gui.mainloop()
