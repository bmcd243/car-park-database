from tkinter import *
from tkinter import ttk
import os
import sys
import time
import tkinter.font as tkFont
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x1000")
root.title("Collyer's Car Park")

def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)

def staff():
	print("")

def visitor():
	print("")

def student():
	print("")

welcome = Label(root, text="Hello, please use the menu above to navigate the interface")
welcome.pack()

### create menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_1 = Menu(menu_bar)
menu_bar.add_cascade(label="Select who you are", menu=menu_1)
menu_1.add_command(label="Caeser Cipher", command=staff)
menu_1.add_command(label="Vernam Cipher", command=student)
menu_1.add_command(label="Symmetric and Asymmetric encryption", command=visitor)
menu_1.add_command(label="Restart Program", command=restart)


staff_frame = Frame(root, width=1000, height=800)
visitor_frame = Frame(root, width=1000, height=800)
student_frame = Frame(root, width=1000, height=800)


root.mainloop()