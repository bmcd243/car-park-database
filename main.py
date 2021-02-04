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
current_today = current_date.strftime("%w")
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

def create_database():
	# define connection and cursor

	connection = sqlite3.connect('collyers_car_park.db')

	cursor = connection.cursor()

	# create details table
	details_table = """CREATE TABLE IF NOT EXISTS
	details(
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
	user_id INTEGER,
	start_date TEXT,
	expiry_date TEXT,
	FOREIGN KEY (user_id) REFERENCES details(user_id))"""
	
	cursor.execute(details_table)
	cursor.execute(booking_table)

	# add default values to details table

	details_default_values = [
		(1,'Bob','Smith','Staff','Lamborgini','Aventador', 'Red', 'RE05 KDJ'),
		(2,'Sarah','McDonald','Staff','Ferrari','LaFerrari', 'Yellow', 'TY07 PER'),
		(3,'Will','Stevenson','Student','Bugatti','Veyron', 'Green', 'RE62 LKD'),
		(4,'Steve','Swimswam','Student','Renault','Clio', 'Pink', 'RE66 KPO'),
		(5,'Harry','Reeto','Visitor','VW','Up!', 'Blue', 'RZ05 FSD'),
	]

	cursor.executemany("INSERT INTO details (user_id, first_name, surname, role, make, model, colour, reg) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", details_default_values)
	connection.commit()

	# add default values to booking table

	booking_default_values = [
		(1, 1, '2021-01-24', '2021-01-24'),
		(2, 2, '2021-01-24', '2021-01-23'),
		(3, 3, '2021-01-24', '2021-01-22'),

	]

	cursor.executemany("INSERT INTO booking (booking_id, user_id, start_date, expiry_date) VALUES (?, ?, ?, ?)", booking_default_values)
	connection.commit()


	print("Default values successfully inserted")

	connection.close()






def booking():

	calendar_frame = Frame(booking_frame)

	### STAFF

	def fetch_staff_names():
		connection = sqlite3.connect('collyers_car_park.db')
		cursor = connection.cursor()

		select_all_staff = ("""SELECT * from details where role='Staff'""")
		cursor.execute(select_all_staff)

		rows = cursor.fetchall()

		staff_list = []

		for row in rows:
			print(row)
			staff_list.append(row)
		print(staff_list)
		
		display_staff_names(staff_list)

		connection.close()

	def display_staff_names(staff_list):
		# combining first and last names
		staff_full_name_list = []
		for i in range(len(staff_list)):
			staff_full_name = staff_list[i][1] + " " + staff_list[i][2]
			staff_full_name_list.append(staff_full_name)


		# filling listbox with staff names
		for i in range(len(staff_list)):
			staff_listbox.insert(END, staff_full_name_list[i])

		staff_listbox.config(yscrollcommand = staff_scroll.set)

		staff_scroll.config(command = staff_listbox.yview)



	### STUDENTS

	def fetch_student_names():
		connection = sqlite3.connect('collyers_car_park.db')
		cursor = connection.cursor()

		select_all_students = ("""SELECT * from details where role='Student'""")
		cursor.execute(select_all_students)

		rows = cursor.fetchall()

		student_list = []

		for row in rows:
			print(row)
			student_list.append(row)
		print(student_list)
		
		display_student_names(student_list)

		connection.close()

	def display_student_names(student_list):
		# combining first and last names
		student_full_name_list = []
		for i in range(len(student_list)):
			student_full_name = student_list[i][1] + " " + student_list[i][2]
			student_full_name_list.append(student_full_name)


		# filling listbox with staff names
		for i in range(len(student_list)):
			student_listbox.insert(END, student_full_name_list[i])

		student_listbox.config(yscrollcommand = student_scroll.set)

		student_scroll.config(command = student_listbox.yview)



	### VISITORS

	def fetch_visitor_names():
		connection = sqlite3.connect('collyers_car_park.db')
		cursor = connection.cursor()

		select_all_visitors = ("""SELECT * from details where role='Visitor'""")
		cursor.execute(select_all_visitors)

		rows = cursor.fetchall()

		visitor_list = []

		for row in rows:
			print(row)
			visitor_list.append(row)
		print(visitor_list)
		
		display_visitor_names(visitor_list)

		connection.close()

	def display_visitor_names(visitor_list):
		# combining first and last names
		visitor_full_name_list = []
		for i in range(len(visitor_list)):
			visitor_full_name = visitor_list[i][1] + " " + visitor_list[i][2]
			visitor_full_name_list.append(visitor_full_name)


		# filling listbox with staff names
		for i in range(len(visitor_list)):
			visitor_listbox.insert(END, visitor_full_name_list[i])

		visitor_listbox.config(yscrollcommand = visitor_scroll.set)

		visitor_scroll.config(command = visitor_listbox.yview)


	
	booking_frame.grid()


	name_store = ttk.Notebook(booking_frame, width=1000, height=400)

	staff_tab = ttk.Frame(name_store)
	visitor_tab = ttk.Frame(name_store)
	student_tab = ttk.Frame(name_store)

	name_store.add(staff_tab, text='Staff')
	name_store.add(visitor_tab, text='Visitor')
	name_store.add(student_tab, text='Student')

	name_store.grid(row=0,column=0)

	staff_listbox = Listbox(staff_tab, selectmode=SINGLE, width=600, height=400)
	staff_listbox.grid()
	staff_scroll = Scrollbar(staff_listbox)

	student_listbox = Listbox(student_tab, selectmode=SINGLE, width=600, height=400)
	student_listbox.grid()
	student_scroll = Scrollbar(student_listbox)

	visitor_listbox = Listbox(visitor_tab, selectmode=SINGLE, width=600, height=400)
	visitor_listbox.grid()
	visitor_scroll = Scrollbar(visitor_listbox)

	fetch_staff_names()
	fetch_student_names()
	fetch_visitor_names()

	i_am_a = Label(booking_frame, text="I am a")
	i_am_a.grid(row=1,column=0)

	dropdown_options = [
		"Staff",
		"Student",
		"Visitor"
	]
	variable = StringVar(booking_frame)
	variable.set(dropdown_options[0])

	dropdown = OptionMenu(booking_frame, variable, *dropdown_options)
	dropdown.grid(row=2, column=0, pady=2)

	select_profession = ttk.Button(booking_frame, text="CONFIRM ROLE")
	select_profession.grid(row=3, column=0)

	if variable == "Staff":
		chosen_name = staff_listbox.get(ACTIVE)
	elif variable == "Student":
		chosen_name = student_listbox.get(ACTIVE)
	else:
		chosen_name = visitor_listbox.get(ACTIVE)

	

	select_name = ttk.Button(booking_frame, text="Select name", command = lambda: display_calendar(chosen_name))
	select_name.grid(row=1, column=0, sticky = W, pady = 2)

	# Fetch details for calendar

	def display_calendar(selected_name):
		calendar_frame.tkraise()

		calendar_instruction = Label(booking_frame, text = "Hi" + selected_name + "Please select a date from the calendar below:")
		calendar_instruction.grid(row=0,column=0)

		# create calendar
		cal = Calendar(booking_frame, selectmode="day", year=int(current_year), month=int(current_month), day=int(current_today))
		cal.grid(row=1,column=0)

		def fetch_date():
			selected_date = cal.get_date()
			print(selected_date)


		book_button = ttk.Button(booking_frame, commmand = lambda: fetch_date())
		book_button.grid(row=3,column=0)










def to_database(profession, make, model, colour, reg):

	connection = sqlite3.connect('collyers_car_park.db')

	cursor = connection.cursor()

	id = "001"

	cursor.execute("INSERT INTO car_park (id, make, model, colour, reg) VALUES (?, ?, ?, ?, ?)", (id, make, model, colour, reg))

	cursor.execute("SELECT * FROM car_park")

	results = cursor.fetchall()
	print(results)



def register():
	register_frame.grid()
	
	welcome = Label(root, text="New user - enter your details below to use the Collyer's car park.")
	welcome.grid()

	# entry text
	first_name = Label(register_frame, text="First name")
	surname = Label(register_frame, text="Surname")
	select_text = Label(register_frame, text="Role")
	make_text = Label(register_frame, text="Make")
	model_text = Label(register_frame, text="Model")
	colour_text = Label(register_frame, text="Colour")
	reg_text = Label(register_frame, text="Reg number")

	select_text.grid(row = 1, column = 0, sticky = W, pady = 2)
	first_name.grid(row = 2, column = 0, sticky = W, pady = 2)
	surname.grid(row = 3, column = 0, sticky = W, pady = 2)
	make_text.grid(row = 4, column = 0, sticky = W, pady = 2)
	model_text.grid(row = 5, column = 0, sticky = W, pady = 2)
	colour_text.grid(row = 6, column = 0, sticky = W, pady = 2)
	reg_text.grid(row = 7, column = 0, sticky = W, pady = 2)


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

	first_name_entry = Entry(register_frame)
	first_name_entry.grid(row=2, column=1, pady=2)

	last_name_entry = Entry(register_frame)
	last_name_entry.grid(row=3, column=1, pady=2)

	make_entry = Entry(register_frame)
	make_entry.grid(row=4, column=1, pady=2)

	model_entry = Entry(register_frame)
	model_entry.grid(row=5, column=1)

	colour_entry = Entry(register_frame)
	colour_entry.grid(row=6, column=1)

	reg_entry = Entry(register_frame)
	reg_entry.grid(row=7, column=1)

	#TODO - create user button, triggers userID creation

	def create_id():
		print("")
	
		def fetch_latest_id():
			connection = sqlite3.connect('collyers_car_park.db')
			cursor = connection.cursor()
			latest_id = cursor.execute("""SELECT * 
			FROM    car_park
			WHERE   ID = (SELECT MAX(ID)  FROM car_park""")
			connection.close()
			print(latest_id)
			
		
		fetch_latest_id()



	register_button = ttk.Button(register_frame, text='Register',command=create_id)
	register_button.grid(row=8, column=1)






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

# create_database()


root.mainloop()