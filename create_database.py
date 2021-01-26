### file to create the database

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

def start_database():
	# define connection and cursor

	connection = sqlite3.connect('collyers_car_park.db')

	cursor = connection.cursor()

	# create stores table

	car_park = """CREATE TABLE IF NOT EXISTS
	car_park(
	id TEXT PRIMARY KEY,
	profession TEXT,
	make TEXT,
	model TEXT,
	colour TEXT,
	reg TEXT,
	date TEXT)"""

	cursor.execute(car_park)

	# add default values to table

	default_values = [
		('1','Staff','Lamborgini','Aventador','Red',today),
		('2','Student','VW','Golf','Yellow',today),
		('3','Visitor','Audi','R8','Blue',today),
		('4','Staff','Renault','Clio','Green',today),
		('5','Student','Vauxhall','Corsa','Pink',today),
	]

	cursor.execute("INSERT INTO car_park (id, profession, make, model, colour, reg, date) VALUES (?, ?, ?, ?, ?)", default_values)



	connection.close()