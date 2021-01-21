from tkinter import *
from tkinter import ttk
import os
import sys
import time
import tkinter.font as tkFont
from PIL import ImageTk, Image

root = Tk()
root.geometry("1000x800")
root.title("Collyer's Car Park")

def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)

def photo_display():
	image_1 = ImageTk.PhotoImage(Image.open("./images/lambo.jpg"))
	photo = Label(main_frame, image = image_1)
	photo.image = image_1
	photo.grid(row=6, column=4, sticky=E, pady=2)

def display():

	photo_display()

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
	print("")







main_frame = Frame(root, width=1000, height=800)
main_frame.grid()

welcome = Label(main_frame, text="Hello, please use the menu above to navigate the interface")
welcome.grid(row=0, column=3)

display()


root.mainloop()