#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter as tk
from spreadsheet_reader import *

class Hospitality(tk.Tk):
	def __init__(self,parent):
		tk.Tk.__init__(self,parent)
		self.parent = parent
		self.people = read_csv('conference.csv')
		self.initialize()

		self.listbox.bind('<<ListboxSelect>>',self.on_select)

	def initialize(self):
		self.minsize(width=1080, height=600)
		self.maxsize(width=1080, height=600)
		self.grid()

		self.label = tk.Label(self,text='')
		self.label.grid(column=0,row=1,sticky='N')
		self.label.configure(state='disabled')

		self.listbox = tk.Listbox(self,width=25,height=34)
		self.listbox.grid(column=0,row=0,sticky='W')
		for i in self.people:
			self.listbox.insert(tk.END,i.label())
		
		# self.grid_columnconfigure(0,weight=1)

	def on_select(self,e):
		# Note here that Tkinter passes an event object to on_select()
		w = e.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		self.label.config(text=str(self.people[index]))

	
		

if __name__ == "__main__":
	app = Hospitality(None)
	app.title('Hospitality :)')
	app.mainloop()