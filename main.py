import os
from tkinter import *
from tkinter import filedialog as fd
directory = r"C:\Program Files (x86)\Steam\steamapps\common\Titanfall2\NorthstarLauncher.exe"  # Update with the correct application path



def change_directory():
    global directory
    filetypes = (
        ('executable files', '*.exe'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Select Northstar Launcher',
        initialdir='/',
        filetypes=filetypes
    )
    if filename: # if a file is selected
        directory = filename # update the directory
        entry.delete(0, END) # clear the entry box
        entry.insert(0, "Directory changed successfully!") # show a message

# Function to start Northstar
def start_northstar():
    try:
        print(directory)
        os.startfile(directory)
    except:
        show_error()

# Function to show error label and change directory
def show_error():
    global directory
    lbl1 = Label(root, text="Failed to Start Northstar!")
    lbl1.pack(side=BOTTOM, anchor=S)

# Function to start Northstar after a delay
def start():
    root.after(0, start_northstar)

root = Tk()
root.title("Thunderbird 0.2")
root.state('zoomed')
root.geometry("1920x1080")

lbl = Label(root, text="Thunderbird is a Northstar Launcher and soon to be a Mod manager.")
lbl.pack()

btn = Button(root, text="Start Northstar", fg="Blue", command=start)
btn.pack(side=BOTTOM, anchor=S)

entry = Entry(root)
entry.pack_forget()  # Remove the entry box

change_button = Button(root, text="Locate Northstar", fg="Red", command=change_directory)
change_button.pack(side=TOP, anchor=E)

root.mainloop()