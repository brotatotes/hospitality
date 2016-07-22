#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter as tk
from spreadsheet_reader import *

class Hospitality(tk.Tk):
	def __init__(self,parent):
		tk.Tk.__init__(self,parent)
		self.parent = parent
		self.people = read_people('BB89RT8239.csv')
		self.hosts = read_hosts('AFSB8ASD8F32.csv')
		self.initialize()

		self.listbox_people.bind('<<ListboxSelect>>',self.on_select_listbox_people)
		self.listbox_hosts.bind('<<ListboxSelect>>',self.on_select_listbox_hosts)
		
		a = Assign(self.people,self.hosts)
		h = a.assign_people()
		for i in h:
			print i.people

	def initialize(self):
		self.minsize(width=1080, height=600)
		self.maxsize(width=1080, height=600)
		self.grid()

		self.label_people = tk.Label(self,text='Select an attendee.',wraplength=500)
		self.label_people.grid(column=1,row=0,sticky='N')
		self.label_people.configure(state='disabled')

		self.listbox_people = tk.Listbox(self,width=25,height=30)
		self.listbox_people.grid(column=0,row=0,rowspan=20,sticky='W')
		for i in self.people:
			self.listbox_people.insert(tk.END,i.label())

		self.label_hosts = tk.Label(self,text='Select a host.',wraplength=500)
		self.label_hosts.grid(column=1,row=1,sticky='N')
		self.label_hosts.configure(state='disabled')
		
		self.listbox_hosts = tk.Listbox(self,width=35,height=30)
		self.listbox_hosts.grid(column=2, row=0,rowspan=20,sticky='W')
		for i in self.hosts:
			self.listbox_hosts.insert(tk.END,i.label())

		self.grid_columnconfigure(1,minsize=536)		

	def on_select_listbox_people(self,e):
		# Note here that Tkinter passes an event object to on_select()
		w = e.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		self.label_people.config(text=str(self.people[index]))

	def on_select_listbox_hosts(self,e):
		# Note here that Tkinter passes an event object to on_select()
		w = e.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		self.label_hosts.config(text=str(self.hosts[index]))


class Assign:
	def __init__(self,people,hosts):
		self.people = people
		self.hosts = hosts

	def assign_people(self):
		sorted_people = sorted(self.people, key=lambda x: len(x.preferences))
		for p in sorted_people:
			if not p.assigned:
				for h in self.hosts:
					if(h.assign(p)):
						break
		return self.hosts




	
		

if __name__ == "__main__":
	app = Hospitality(None)
	app.title('Hospitality :)')
	app.mainloop()