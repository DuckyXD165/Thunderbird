import os
import shutil
import requests
import zipfile
import webbrowser
from tkinter import *
from tkinter import filedialog as fd

directory = r"C:\Program Files (x86)\Steam\steamapps\common\Titanfall2\NorthstarLauncher.exe"
URL = "https://github.com/R2Northstar/Northstar/releases/download/v1.23.0/Northstar.release.v1.23.0.zip"


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
        webbrowser.open('steam://rungameid/1237970')
    except:
        try:
            os.startfile(directory)
        except:
            show_error("Failed to start Northstar!")


def unpack_northstar():
    with zipfile.ZipFile('Northstar.release.v1.23.0.zip', 'r') as zip_ref:
        zip_ref.extractall()


def prep_northstar():
    try:
        if os.path.isdir(directory):
            grab_northstar()
            unpack_northstar()
            start_northstar()
        else:
            raise FileNotFoundError("Selected directory does not exist.")
    except Exception as e:
        show_error(str(e))


def grab_northstar():
    try:
        response = requests.get(URL)
    except OSError:
        print('No connection to the server!')
        raise
    if response.status_code == 200:
        print('Status 200, OK')
        open('Northstar.release.v1.23.0.zip', 'wb').write(response.content)
    else:
        print('ZIP file request not successful!')
        raise


def show_error(error_message):
    lbl1 = Label(root, text=f"Error: {error_message}")
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
install_button = Button(root, text="Install Northstar", fg="Red", command=prep_northstar)
install_button.pack(side=TOP, anchor=E)
root.mainloop()