import sqlite3
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk
from enum import Enum
from PIL import Image, ImageTk
from tkinter import simpledialog

root5 = Tk()
root5.title("Memo")
root5.geometry("450x640+600+200")
root5.withdraw()
canvass = Canvas(root5, width=360, height=60, bg="#BC4CD0", bd=0, highlightthickness=0)
canvass.pack(fill='x')
label = Label(root5, text="MEMO", bg="#BC4CD0", fg="white", font=("Inter", 20, "bold"))
label.place(x=330, y=10)
textbox6 = Text(root5, wrap='word', font=("Arial", 12), width=31, height=2, bd=1, relief="raised")
textbox6.place(x=80,y=80)
label = Label(root5, text="Title:", bg=None, fg="black", font=("Inter", 12, "bold"))
label.place(x=8, y=85)

def add_item2(x,y):
    text = x
    if text:
        var = IntVar()
        item = {"text": (text if len(text) < 25 else text[:25] + "\n" + text[25:]), "checked": 0}
        itemss.append(item)
        create_item_widgett2(item,y)
        entry_box.delete(0, END)

def create_item_widgett2(item,y):
    framee = Frame(canvasq_frame, bg="#FCD2F4", bd=0)
    framee.pack(fill="x", pady=2)
    var = BooleanVar(value=item["checked"])
    item["checked"] = var
    item["checked"] = 0
    checkbox = Checkbutton(framee, variable=var, command=lambda: toggle_checkboxx(item), bg="#FCD2F4", bd=0)
    checkbox.pack(side=LEFT)
    if (y==1):
        checkbox.invoke()
        y=0
    text_label = Label(framee, text=item["text"], anchor="w", bg="#FCD2F4", bd=0)
    text_label.pack(side=LEFT, expand=True, fill="x", padx=5)

    modify_button = Button(framee, text="Modifica", command=lambda: modify_itemm(item, text_label), bg="#FCD2F4", bd=0,
                           fg="green", font=("Arial", 10, "bold"))
    modify_button.pack(side=RIGHT, padx=5)

    delete_button = Button(framee, text="Sterge", command=lambda: delete_itemm(item, framee), bg="#FCD2F4", bd=0,
                           fg="red", font=("Arial", 10, "bold"))
    delete_button.pack(side=RIGHT, padx=5)


def toggle_checkboxx2(item):
    if(item["checked"]==1):
        item["checked"]=0
    else:
        item["checked"]=1

def add_itemm():
    text = entry_box.get().strip()[:50]
    if text:
        var = IntVar()
        item = {"text": (text if len(text)<25 else text[:25]+"\n"+text[25:]), "checked": 0}
        itemss.append(item)
        create_item_widgett(item)
        entry_box.delete(0, END)

def modify_itemm(item, text_label):
    new_text = simpledialog.askstring("Modify Element", "Introduceti noul text:")
    if new_text:
        item["text"] = new_text
        text_label.config(text=new_text)

def delete_itemm(item, frame):
    itemss.remove(item)
    frame.destroy()
    canvasq_frame.configure(background="#FCD2F4")

def toggle_checkboxx(item):
    if(item["checked"]==1):
        item["checked"]=0
    else:
        item["checked"]=1

def create_item_widgett(item):
    framee = Frame(canvasq_frame,bg="#FCD2F4",bd=0)
    framee.pack(fill="x", pady=2)
    var = BooleanVar(value=item["checked"])
    item["checked"]=var
    item["checked"] = 0
    checkbox = Checkbutton(framee, variable=var, command=lambda: toggle_checkboxx(item),bg="#FCD2F4",bd=0)
    checkbox.pack(side=LEFT)

    text_label = Label(framee, text=item["text"], anchor="w",bg="#FCD2F4",bd=0)
    text_label.pack(side=LEFT, expand=True, fill="x", padx=5)

    modify_button = Button(framee, text="Modifica", command=lambda: modify_itemm(item, text_label),bg="#FCD2F4",bd=0,fg="green",font=("Arial", 10, "bold"))
    modify_button.pack(side=RIGHT, padx=5)

    delete_button = Button(framee, text="Sterge", command=lambda: delete_itemm(item, framee),bg="#FCD2F4",bd=0,fg="red",font=("Arial", 10, "bold"))
    delete_button.pack(side=RIGHT, padx=5)


canvasq = Canvas(root5,bd=2, relief="solid" ,bg="#FCD2F4")
canvasq.place(x=20, y=240,width=400, height=300)
scrollbar = Scrollbar(root5, orient="vertical", command=canvasq.yview)
scrollbar.place(x=420, y=240, height=300)
canvasq.configure(yscrollcommand=scrollbar.set)
canvasq_frame = Frame(canvasq)
canvasq.create_window((0, 0), window=canvasq_frame, anchor="nw")
canvasq_frame.bind("<Configure>", lambda e: canvasq.config(scrollregion=canvasq.bbox("all")))
entry_box = Entry(root5, width=30)
entry_box.place(x=100, y=180)
add_button = Button(root5, text="Adaugă", bg="#BC4CD0", fg="white", command=add_itemm)
add_button.place(x=20, y=180)

itemss = []

