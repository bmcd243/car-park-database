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

# fetching dates
current_date = datetime.datetime.now()
current_today = current_date.strftime("%w")
current_month = current_date.strftime("%m")
current_year = current_date.strftime("%Y")
full_date = datetime.date.today()

def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)



# define self
class tkinterApp(Tk):

	def __init__(self,*args, **kwargs):

		Tk.__init__(self, *args, **kwargs)

		# creating a container
		container = Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initialising frames to an empty array
		self.frames = {}

		menu_bar = Menu(container)
		main_menu = Menu(menu_bar)

		menu_bar.add_cascade(label="Main Menu", menu=main_menu)
		main_menu.add_command(label="Welcome page", command=lambda: self.show_frame(welcome_frame))
		main_menu.add_command(label="Book a vehicle", command=lambda: self.show_frame(booking_frame))
		main_menu.add_command(label="Register as new user", command=lambda: self.show_frame(register_frame))
		main_menu.add_command(label="Restart", command= restart)

		Tk.config(self, menu=menu_bar)

		for F in (welcome_frame, booking_frame, register_frame, calendar_frame, calendar_frame_2, confirmation_frame):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame(welcome_frame)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


class welcome_frame(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# display photo on screen
		def photo_display():
			image_1 = ImageTk.PhotoImage(Image.open("./images/lambo.jpg"))
			photo = Label(self, image = image_1)
			photo.image = image_1
			photo.grid(row=6, column=4, sticky=E, pady=2)
		
		photo_display()


		welcome = Label(self, text="Hello, please use the menu above to navigate the interface")
		welcome.grid(row=0, column=4, padx=10, pady=10)

class register_frame(Frame):

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)

		welcome = Label(self, text="New user - enter your details below to use the Collyer's car park.")
		welcome.grid()

		# entry text
		first_name = Label(self, text="First name")
		surname = Label(self, text="Surname")
		select_text = Label(self, text="Role")
		make_text = Label(self, text="Make")
		model_text = Label(self, text="Model")
		colour_text = Label(self, text="Colour")
		reg_text = Label(self, text="Reg number")

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
		variable = StringVar(self)
		variable.set(dropdown_options[0])

		dropdown = OptionMenu(self, variable, *dropdown_options)
		dropdown.grid(row=1, column=1, pady=2)

		first_name_entry = Entry(self)
		first_name_entry.grid(row=2, column=1, pady=2)

		last_name_entry = Entry(self)
		last_name_entry.grid(row=3, column=1, pady=2)

		make_entry = Entry(self)
		make_entry.grid(row=4, column=1, pady=2)

		model_entry = Entry(self)
		model_entry.grid(row=5, column=1)

		colour_entry = Entry(self)
		colour_entry.grid(row=6, column=1)

		reg_entry = Entry(self)
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



		register_button = ttk.Button(self, text='Register',command=create_id)
		register_button.grid(row=8, column=1)




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


class booking_frame(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		

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


		name_store = ttk.Notebook(self, width=1000, height=400)

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

		i_am_a = Label(self, text="Select your name from the list above and confirm your role: ")
		i_am_a.grid(row=1,column=0)

		dropdown_options = [
			"Staff",
			"Student",
			"Visitor"
		]
		variable = StringVar(self)
		variable.set(dropdown_options[0])

		dropdown = OptionMenu(self, variable, *dropdown_options)
		dropdown.grid(row=2, column=0, pady=2)

		select_name = ttk.Button(self, text="Select name", command=lambda: confirm_role())
		select_name.grid(row=4, column=0, pady = 2)

		self.chosen_name = ''

		def confirm_role():
			chosen_role = variable.get()
			print(chosen_role)
			if chosen_role == "Staff":
				self.chosen_name = staff_listbox.get(ACTIVE)
			elif chosen_role == "Student":
				self.chosen_name = student_listbox.get(ACTIVE)
			else:
				self.chosen_name = visitor_listbox.get(ACTIVE)

			print("role confirmed, name is " + self.chosen_name)

			success = Label(self, text="You're name has been successfully selected. Press the button below to move to the calendar.")
			success.grid(row=5, column=0, pady=2)

			move_to = ttk.Button(self, text="MOVE TO CALENDAR", command = lambda: go_to_calendar())
			move_to.grid(row=6, column=0, pady=2)

			def go_to_calendar():
				controller.show_frame(calendar_frame)			
			

class calendar_frame(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		def calendar_display():

			print("LOOK, " + controller.frames[booking_frame].chosen_name)

			go_back = Button(self, text="<--", command=lambda: controller.show_frame(booking_frame))
			go_back.grid(column=0, row=0, sticky = NW)

			calendar_instruction = Label(self, text = "Hi " + controller.frames[booking_frame].chosen_name + ", please select a start date:")
			calendar_instruction.grid(row=1,column=1)

			# create calendar
			cal = Calendar(self, selectmode="day", year=int(current_year), month=int(current_month), day=int(current_today))
			cal.grid(row=2,column=1)

			self.start_date = ''

			def fetch_date():
				self.start_date = cal.get_date()
				print(self.start_date)
				controller.show_frame(calendar_frame_2)

			book_button = ttk.Button(self, text='Confirm date', command=fetch_date)
			book_button.grid(row=3,column=0)
			
		calendar_display()

class calendar_frame_2(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		def calendar_2_display():

			go_back = Button(self, text="<--", command=lambda: controller.show_frame(calendar_frame))
			go_back.grid(column=0, row=0, sticky = NW)

			calendar_instruction = Label(self, text = controller.frames[booking_frame].chosen_name + ", you will be booked in from" + controller.frames[calendar_frame].start_date + ". Please select an expiry date:")
			calendar_instruction.grid(row=1,column=1)

			# create calendar
			cal = Calendar(self, selectmode="day", year=int(current_year), month=int(current_month), day=int(current_today))
			cal.grid(row=2,column=1)

			self.expire_date = ''

			def fetch_date():
				self.expire_date = cal.get_date()
				print(self.expire_date)
				controller.show_frame(confirmation_frame)

			book_button = ttk.Button(self, text='Confirm date', command=fetch_date)
			book_button.grid(row=3,column=0)

		calendar_2_display()

class confirmation_frame(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		go_back = Button(self, text="<--", command=lambda: controller.show_frame(calendar_frame_2))
		go_back.grid(column=0, row=0, sticky = NW)

		name = controller.frames[booking_frame].chosen_name
		start_date_final = controller.frames[calendar_frame].start_date
		expire_date_final = controller.frames[calendar_frame_2].expire_date


		confirmation_label = Label(self, text="Perfect, " + name + "you're vehicle is booked in from" + start_date_final + " until " + expire_date_final)
		confirmation_label.grid()






# photo_display()

# create_database()


app = tkinterApp()
app.geometry("1000x800")
app.title("Collyer's Car Park")
app.mainloop()



