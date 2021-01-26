# import tkinter modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkcalendar import *

# import modules for restart functionality
import os
import sys
import time

# import sqlite 3 for database functionality
import sqlite3

# import datetime module
import datetime



# define root
root = Tk()
root.geometry("1000x800")
root.title("Collyer's Car Park")

# fetching dates
current_date = datetime.datetime.now()
current_today = current_date.strftime("%A")
current_month = current_date.strftime("%m")
current_year = current_date.strftime("%Y")
full_date = datetime.date.today()

def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)


# display photo on screen
# def photo_display():
# 	image_1 = ImageTk.PhotoImage(Image.open("./images/lambo.jpg"))
# 	photo = Label(main_frame, image = image_1)
# 	photo.image = image_1
# 	photo.grid(row=6, column=4, sticky=E, pady=2)

def start_database():
	# define connection and cursor

	connection = sqlite3.connect('collyers_car_park.db')

	cursor = connection.cursor()

	# create details table
	details_table = """CREATE TABLE IF NOT EXISTS
	register(
	user_id INTEGER PRIMARY KEY,
	first_name TEXT,
	surname TEXT,
	role TEXT,
	make TEXT,
	model TEXT,
	colour TEXT,
	reg TEXT)"""

	# create booking table
	booking_table = """CREATE TABLE IF NOT EXISTS
	booking(
		booking_id INTEGER PRIMARY KEY,
		FOREIGN KEY (user_id)
		REFERENCES details_table(booking_id)
		start_date TEXT,
		expiry_date TEXT)"""

	# create tables
	cursor.execute(details_table)
	cursor.execute(booking_table)

	# add default values to table

	details_default_values = [
		('1','Bob','Smith','Staff','Lamborgini','Aventador', 'Red', 'RE05 KDJ'),
		('2','Sarah','McDonald','Staff','Ferrari','LaFerrari', 'Yellow', 'TY07 PER'),
		('3','Will','Stevenson','Student','Bugatti','Veyron', 'Green', 'RE62 LKD'),
		('4','Steve','Swimswam','Student','Renault','Clio', 'Pink', 'RE66 KPO'),
		('5','Harry','Reeto','Visitor','VW','Up!', 'Blue', 'RZ05 FSD'),
	]

	cursor.execute("INSERT INTO details_table (user_id, first_name, surname, role, make, model, colour, reg) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", details_default_values)

	booking_default_values = [
		('1', '1', full_date, '2021-01-24'),
		('2', '2', full_date, '2021-01-23'),
		('3', '3', full_date, '2021-01-22')

	]

	cursor.execute("INSERT INTO booking_table (booking_id, user_id, start_date TEXT, expiry_date TEXT) VALUES (?, ?, ?, ?)", booking_default_values)



	connection.close()



def booking():
	booking_frame.pack()

	name_store = ttk.Notebook(booking_frame, width=1000, height=600)

	staff_tab = ttk.Frame(name_store)
	visitor_tab = ttk.Frame(name_store)
	student_tab = ttk.Frame(name_store)

	name_store.add(staff_tab,)


	# create calendar
	cal = Calendar(booking_frame, selectmode="day", year=current_year, month=current_month, day=current_today)
	cal.grid()





	confirm_button = ttk.Button(booking_frame, text="Book car", command= to_database)
	confirm_button.grid(row=6, column=1)




def to_database(profession, make, model, colour, reg):

	connection = sqlite3.connect('collyers_car_park.db')

	cursor = connection.cursor()

	id = "001"

	cursor.execute("INSERT INTO car_park (id, make, model, colour, reg) VALUES (?, ?, ?, ?, ?)", (id, make, model, colour, reg))

	cursor.execute("SELECT * FROM car_park")

	results = cursor.fetchall()
	print(results)



def register():
	register_frame.pack()
	
	welcome = Label(root, text="New user - enter your details below to use the Collyer's car park.")
	welcome.pack()

	# entry text
	first_name = Label(register_frame, text="First name")
	surname = Label(register_frame, text="Surname")
	select_text = Label(register_frame, text="Role")
	make_text = Label(register_frame, text="Make")
	model_text = Label(register_frame, text="Model")
	colour_text = Label(register_frame, text="Colour")
	reg_text = Label(register_frame, text="Reg number")


	select_text.grid(row = 1, column = 0, sticky = W, pady = 2)
	make_text.grid(row = 2, column = 0, sticky = W, pady = 2)
	model_text.grid(row = 3, column = 0, sticky = W, pady = 2)
	colour_text.grid(row = 4, column = 0, sticky = W, pady = 2)
	reg_text.grid(row = 5, column = 0, sticky = W, pady = 2)


	# entry fields
	dropdown_options = [
		"Staff",
		"Student",
		"Visitor"
	]
	variable = StringVar(register_frame)
	variable.set(dropdown_options[0])

	dropdown = OptionMenu(register_frame, variable, *dropdown_options)
	dropdown.grid(row=1, column=1, pady=2)

	make_entry = Entry(register_frame)
	make_entry.grid(row=2, column=1, pady=2)

	model_entry = Entry(register_frame)
	model_entry.grid(row=3, column=1)

	colour_entry = Entry(register_frame)
	colour_entry.grid(row=4, column=1)

	reg_entry = Entry(register_frame)
	reg_entry.grid(row=5, column=1)

	#TODO - create user button, triggers userID creation






welcome_frame = Frame(root, width=1000, height=800)
welcome_frame.grid()

welcome = Label(welcome_frame, text="Hello, please use the menu above to navigate the interface")
welcome.grid()

register_frame = Frame(root, width=1000, height=800)
booking_frame = Frame(root, width=1000, height=800)

### create menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_1 = Menu(menu_bar)
menu_bar.add_cascade(label="Main Menu", menu=menu_1)
menu_1.add_command(label="Book a vehicle", command=booking)
menu_1.add_command(label="Register as new user", command=register)
menu_1.add_command(label="Restart Program", command=restart)

# photo_display()


root.mainloop()





# def fetch_latest_id():
# 	cursor.execute(SELECT * 
# 		FROM    car_park
# 		WHERE   ID = (SELECT MAX(ID)  FROM car_park);


# def create_id(profession, latest_id):
# 	if profession == "Student":
# 		id = "stu" + latest_id
# 	if profession == "Staff":
# 		id = "sta" + latest_id
# 	if profession == "Visitor":
# 		id = "vis" + latest_id

# fetch_latest_id()
# create_id()