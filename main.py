import os
from tkinter import *
from tkinter import filedialog as fd
directory = r"C:\Program Files (x86)\Steam\steamapps\common\Titanfall2\NorthstarLauncher.exe" 

def change_directory():
    global directory
    filetypes = (
        ('executable files', '*.exe'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Select Northstar Launcher',
        initialdir='C:/Program Files (x86)/Steam/steamapps/common/Titanfall2',
        filetypes=filetypes
    )
    if filename:
        directory = filename
        entry.delete(0, END)
        entry.insert(0, "Directory changed successfully!")
def start_northstar():
    try:
        print(directory)
        os.startfile(directory)
    except:
        show_error()
def show_error():
    global directory
    lbl1 = Label(root, text="Failed to Start Northstar!")
    lbl1.pack(side=BOTTOM, anchor=S)
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
entry.pack_forget()
change_button = Button(root, text="Locate Northstar", fg="Red", command=change_directory)
change_button.pack(side=TOP, anchor=E)

root.mainloop()