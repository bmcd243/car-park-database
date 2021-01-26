### allows existing user to create a new booking

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

# create calendar
cal = Calendar(root, selectmode="day", year=today.year(), )

def fetch_details():
	profession = variable.get()
	make = make_entry.get()
	model = model_entry.get()
	colour = colour_entry.get()
	reg = reg_entry.get()

	to_database(profession, make, model, colour, reg)

	confirm_button = ttk.Button(main_frame, text="Confirm", command= fetch_details)
	confirm_button.grid(row=6, column=1)




def to_database(profession, make, model, colour, reg):

	id = "001"

	cursor.execute("INSERT INTO car_park (id, make, model, colour, reg) VALUES (?, ?, ?, ?, ?)", (id, make, model, colour, reg))

	cursor.execute("SELECT * FROM car_park")

	results = cursor.fetchall()
	print(results)