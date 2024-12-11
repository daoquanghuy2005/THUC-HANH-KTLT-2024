from tkinter import *

# Hàm xử lý cho các mục trong menu
def NewFile():
    print("New File!")

def OpenFile():
    print("Open File!")

def Exit():
    print("Exiting application...")
    root.quit()

def InsText():
    print("Insert Text!")

def InsPic():
    print("Insert Picture!")

def About():
    print("This is a simple example of a menu")

# Tạo cửa sổ chính
root = Tk()
root.title("Menu Example")

# Tạo menu
menu = Menu(root)
root.config(menu=menu)

# Menu "File"
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# Menu "Insert"
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# Menu "Help"
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# Vòng lặp chính
root.mainloop()
