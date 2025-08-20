from tkinter import ttk
from tkinter import *
from tkinter import simpledialog


root=Tk()
root.title("Memo")
root.geometry("450x640+600+200")
canvas = Canvas(root, width=360, height=60, bg="#BC4CD0", bd=0, highlightthickness=0)
canvas.pack(fill='x')
canvas.create_line(0, 60, 360, 60, fill="gray", width=3)
label = Label(root, text="MEMO",bg="#BC4CD0",fg="white", font=("Inter", 20,"bold"))
label.place(x=10, y=10)
main_frame= Frame(root)
main_frame.pack(fill=BOTH,expand=1)
my_canvas= Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
my_scroll=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scroll.pack(side=RIGHT,fill=Y)
my_canvas.configure(yscrollcommand=my_scroll.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame=Frame(my_canvas)
my_canvas.create_window((0,0),window=second_frame,anchor="nw")


root2 = Tk()
root2.title("Memo")
root2.geometry("450x640+600+200")
canvas = Canvas(root2, width=360, height=60, bg="#BC4CD0", bd=0, highlightthickness=0)
canvas.pack(fill='x')
canvas.create_line(0, 60, 360, 60, fill="gray", width=3)
label = Label(root2, text="MEMO", bg="#BC4CD0", fg="white", font=("Inter", 20, "bold"))
label.place(x=330, y=10)
frame = Frame(root2, width=440, height=400)
frame.place(x=5, y=150)
frame.pack_propagate(False)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
textbox1 = Text(frame, wrap='word', yscrollcommand=scrollbar.set, font=("Arial", 12), width=38, height=10,bd=2,  relief="raised")  # Ajustăm lățimea și înălțimea
textbox1.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=textbox1.yview)
textbox2 = Text(root2, wrap='word', font=("Arial", 12), width=31, height=2, bd=1, relief="raised")
label = Label(root2, text="Title:", bg=None, fg="black", font=("Inter", 12, "bold"))
label.place(x=8, y=85)
root2.withdraw()



root3 = Tk()
root3.title("Memo")
root3.geometry("450x640+600+200")
canvas = Canvas(root3, width=360, height=60, bg="#BC4CD0", bd=0, highlightthickness=0)
canvas.pack(fill='x')
canvas.create_line(0, 60, 360, 60, fill="gray", width=3)
label = Label(root3, text="MEMO", bg="#BC4CD0", fg="white", font=("Inter", 20, "bold"))
label.place(x=330, y=10)
frame = Frame(root3, width=440, height=400)
frame.place(x=5, y=150)
frame.pack_propagate(False)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
textbox3 = Text(frame, wrap='word', yscrollcommand=scrollbar.set, font=("Arial", 12), width=38, height=10,bd=2,  relief="raised")  # Ajustăm lățimea și înălțimea
textbox3.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=textbox1.yview)
textbox4 = Text(root3, wrap='word', font=("Arial", 12), width=31, height=2, bd=1, relief="raised")
textbox4.place(x=80,y=80)
label = Label(root3, text="Title:", bg=None, fg="black", font=("Inter", 12, "bold"))
label.place(x=8, y=85)
root3.withdraw()




def add_item():
    text = entry_box.get().strip()[:50]
    if text:
        var = IntVar()
        item = {"text": (text if len(text)<25 else text[:25]+"\n"+text[25:]), "checked": 0}
        items.append(item)
        create_item_widget(item)
        entry_box.delete(0, END)

def modify_item(item, text_label):
    new_text = simpledialog.askstring("Modify Element", "Introduceti noul text:")
    if new_text:
        item["text"] = new_text
        text_label.config(text=new_text)

def delete_item(item, frame):
    items.remove(item)
    frame.destroy()
    canvas_frame.configure(background="#FCD2F4")

def toggle_checkbox(item):
    if(item["checked"]==1):
        item["checked"]=0
    else:
        item["checked"]=1

def create_item_widget(item):
    frame = Frame(canvas_frame,bg="#FCD2F4",bd=0)
    frame.pack(fill="x", pady=2)
    var = BooleanVar(value=item["checked"])
    item["checked"]=var
    item["checked"] = 0
    checkbox = Checkbutton(frame, variable=var, command=lambda: toggle_checkbox(item),bg="#FCD2F4",bd=0)
    checkbox.pack(side=LEFT)

    text_label = Label(frame, text=item["text"], anchor="w",bg="#FCD2F4",bd=0)
    text_label.pack(side=LEFT, expand=True, fill="x", padx=5)

    modify_button = Button(frame, text="Modifica", command=lambda: modify_item(item, text_label),bg="#FCD2F4",bd=0,fg="green",font=("Arial", 10, "bold"))
    modify_button.pack(side=RIGHT, padx=5)

    delete_button = Button(frame, text="Sterge", command=lambda: delete_item(item, frame),bg="#FCD2F4",bd=0,fg="red",font=("Arial", 10, "bold"))
    delete_button.pack(side=RIGHT, padx=5)




root4 = Tk()
root4.title("Memo")
root4.geometry("450x640+600+200")
canvas = Canvas(root4, width=360, height=60, bg="#BC4CD0", bd=0, highlightthickness=0)
canvas.pack(fill='x')
canvas.create_line(0, 60, 360, 60, fill="gray", width=3)
label = Label(root4, text="MEMO", bg="#BC4CD0", fg="white", font=("Inter", 20, "bold"))
label.place(x=330, y=10)
textbox5 = Text(root4, wrap='word', font=("Arial", 12), width=31, height=2, bd=1, relief="raised")
textbox5.place(x=80,y=80)
label = Label(root4, text="Title:", bg=None, fg="black", font=("Inter", 12, "bold"))
label.place(x=8, y=85)
canvas = Canvas(root4,bd=2, relief="solid" ,bg="#FCD2F4")
canvas.place(x=20, y=240,width=400, height=300)
scrollbar = Scrollbar(root4, orient="vertical", command=canvas.yview)
scrollbar.place(x=420, y=240, height=300)
canvas.configure(yscrollcommand=scrollbar.set)
canvas_frame = Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")
canvas_frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))
entry_box = Entry(root4, width=30)
entry_box.place(x=100, y=180)
add_button = Button(root4, text="Adauga", bg="#BC4CD0", fg="white", command=add_item)
add_button.place(x=20, y=180)
items = []
root4.withdraw()




