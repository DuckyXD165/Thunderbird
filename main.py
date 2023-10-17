import os
from tkinter import *

directory = r"C:\Program Files (x86)\Steam\steamapps\common\Titanfall2\NorthstarLauncher.exe"  # Update with the correct application path

# Function to change directory
def change_directory():
    global directory
    directory = entry.get()
    entry.delete(0, END)
    entry.insert(0, "Directory changed successfully!")

# Function to start Northstar
def start_northstar():
    try:
        print(directory)
        os.startfile(f"'{directory}'")
    except:
        show_error()

# Function to show error label and change directory
def show_error():
    global directory
    lbl1 = Label(root, text="Failed to Start Northstar!")
    lbl1.pack(side=BOTTOM, anchor=S)
    change_button.pack(side=BOTTOM, anchor=S)

# Function to start Northstar after a delay
def start():
    root.after(0, start_northstar)

root = Tk()
root.title("Thunderbird 0.1")
root.geometry("1920x1080")

lbl = Label(root, text="Thunderbird is a Northstar Launcher and soon to be a Mod manager.")
lbl.pack()

btn = Button(root, text="Start Northstar", fg="Blue", command=start)
btn.pack(side=BOTTOM, anchor=S)

entry = Entry(root)
entry.pack_forget()  # Remove the entry box

change_button = Button(root, text="Change Directory", command=change_directory)

root.mainloop()