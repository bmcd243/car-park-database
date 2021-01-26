### file to register new user

# import tkinter modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image

# import modules for restart functionality
import os
import sys
import time

# import sqlite 3 for database functionality
import sqlite3

# import datetime module
import datetime

# import other python files used
import register
import booking
import main

def new_user():
	welcome = Label(root, text="New user - enter your details below to use the Collyer's car park.")
	welcome.pack()


def display():

	select_text = Label(main_frame, text="Profession")
	make_text = Label(main_frame, text="Make")
	model_text = Label(main_frame, text="Model")
	colour_text = Label(main_frame, text="Colour")
	reg_text = Label(main_frame, text="Registration")

	select_text.grid(row = 1, column = 0, sticky = W, pady = 2)
	make_text.grid(row = 2, column = 0, sticky = W, pady = 2)
	model_text.grid(row = 3, column = 0, sticky = W, pady = 2)
	colour_text.grid(row = 4, column = 0, sticky = W, pady = 2)
	reg_text.grid(row = 5, column = 0, sticky = W, pady = 2)



	dropdown_options = [
		"Staff",
		"Student",
		"Visitor"
	]
	variable = StringVar(main_frame)
	variable.set(dropdown_options[0])

	dropdown = OptionMenu(main_frame, variable, *dropdown_options)
	dropdown.grid(row=1, column=1, pady=2)

	make_entry = Entry(main_frame)
	make_entry.grid(row=2, column=1, pady=2)

	model_entry = Entry(main_frame)
	model_entry.grid(row=3, column=1)

	colour_entry = Entry(main_frame)
	colour_entry.grid(row=4, column=1)

	reg_entry = Entry(main_frame)
	reg_entry.grid(row=5, column=1)