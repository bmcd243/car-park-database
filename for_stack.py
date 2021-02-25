# import tkinter modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkcalendar import *



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

        Tk.config(self, menu=menu_bar)

        for F in (welcome_frame, booking_frame, register_frame, calendar_frame):
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

        welcome = Label(self, text="Hello, please use the menu above to navigate the interface")
        welcome.grid(row=0, column=4, padx=10, pady=10)

class register_frame(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        register_label = Label(self, text="New user - enter your details below to use the Collyer's car park.")
        register_label.grid()


class booking_frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.chosen_name = "Steve"


class calendar_frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        print(controller.frames[booking_frame].chosen_name)


app = tkinterApp()
app.geometry("1000x800")
app.title("Collyer's Car Park")
app.mainloop()