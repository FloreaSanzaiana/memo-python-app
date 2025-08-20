from grafica import *
from grafica2 import *
from tkinter import messagebox
DB_NAME = "memo.db"

icon2 = PhotoImage(file="../assets/arrow.png")
icon1 = PhotoImage(file="../assets/add_list.png")
icon = PhotoImage(file="../assets/add.png")

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        type TEXT NOT NULL CHECK (type IN ('text', 'list')),
        content TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS list_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        is_completed INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (note_id) REFERENCES notes(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()


class NoteType(Enum):
    TEXT = "text"
    LIST = "list"
class Note:
    def __init__(self):
        self.title = None
        self.type = None
        self.content = None
        self.note_id = None
    def add_note(self, title, type, content):
        pass
    def update_note(self, note_id,title, content):
        pass
    def delete_note(self, note_id):
        pass
    def get_content(self,note_id):
        pass
    def get_type(self,note_id):
        pass
    def get_title(self,note_id):
        pass
    def get_id(self):
        pass

class TextNote(Note):
    def __init__(self):
        super(TextNote, self).__init__()
    def add_note(self, title, type, content):
        self.title = title
        self.type = type
        self.content = content
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO notes (title, type, content)
        VALUES (?,?,?)
        """,(self.title, self.type, self.content))
        self.note_id = cursor.lastrowid
        conn.commit()
        conn.close()
    def delete_note(self, id):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM notes where id=?
        """,(id,))
        conn.commit()
        conn.close()
    def get_note(self, id):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        Select * from notes where id=?
        """,(id,))
        content = cursor.fetchone()
        cursor.close()
        return content
    def update_note(self, idd, title, typee, content):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE notes
        SET title=?,type=?,content=?
        WHERE id=?
        """,(title,typee,content,idd))
        conn.commit()
        conn.close()


class ListNote(Note):
    def __init__(self):
        super(ListNote, self).__init__()
    def delete_note(self, id):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
    DELETE FROM list_items where note_id=?""",(id,)
            )
        cursor.execute("""
            DELETE FROM notes where id=?""", (id,)
                       )
        conn.commit()
        conn.close()
    def get_note(self, id):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
       Select * from list_items join notes on list_items.note_id=notes.id where list_items.note_id=?;""",(id,)
        )
        content = cursor.fetchall()
        cursor.close()
        return content
    def add_note(self, title, type, content):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO notes (title, type, content) values (?,?,?);
        """,(title,type," ")
        )
        my_id=cursor.lastrowid
        for j in content:
            for i in j:
             cursor.execute("""
            INSERT INTO list_items (note_id, content,is_completed) values (?,?,?);""",(my_id,i,j[i])
             )
        conn.commit()
        conn.close()

    def update_note(self,id, title, content):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
              UPDATE notes
            SET title=?,content=?
            WHERE id=?;
              """, (title, " ", id)
                       )
        cursor.execute("""
           DELETE FROM list_items where note_id=?""", (id,)
                       )
        for j in content:
            for i in j:
                cursor.execute("""
                  INSERT INTO list_items (note_id, content,is_completed) values (?,?,?);""", (id, i, j[i]))
        conn.commit()
        conn.close()


def check_note_type(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT type FROM notes WHERE id=?;""",(id,))
    return cursor.fetchone()[0]
    conn.commit()
    conn.close()



def get_all_notes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM notes
    """)
    content = cursor.fetchall()
    cursor.close()
    return content


def add_button_click():
    add_page()
    root.withdraw()
    root3.deiconify()
    textbox4.delete("1.0",END)
    textbox3.delete("1.0", END)

def on_back_list():
    main_page()
    root4.withdraw()
    root5.withdraw()
    root.deiconify()
    textbox5.delete("1.0", END)
    textbox6.delete("1.0", END)
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    canvas_frame.configure(background="#FCD2F4")
    canvas.config(scrollregion=canvas.bbox("all"))

    for widget in canvasq_frame.winfo_children():
        widget.destroy()
    canvasq_frame.configure(background="#FCD2F4")
    canvasq.config(scrollregion=canvasq.bbox("all"))
    main_page()
    itemss.clear()
    items.clear()

def on_save_list():
    elements=[]
    for i in items:
        elements.append({i["text"]:i["checked"]})
    l=ListNote()
    l.add_note(textbox5.get("1.0",END).strip() if len(textbox5.get("1.0",END).strip())>0 else "New Note","list",elements)
    messagebox.showinfo("Save", "The note has been saved.")
    main_page()
def add_list_button_click():
    root.withdraw()
    root4.deiconify()
    itemss.clear()
    items.clear()
    button_save_4 = Button(root4, text="SAVE", command=on_save_list, bg="#BC4CD0", fg="white", bd=0,
                           font=("Arial", 10, "bold"), width=10, height=1, highlightthickness=3,
                           highlightbackground="gray")
    button_save_4.place(x=180, y=580)
    button3 = Button(root4, text="BACK",command=on_back_list, fg="green", font=("Inter", 10, "bold"), bg="white", bd=0)
    button3.place(x=10, y=15)


button_add = Button(root, image=icon,command=add_button_click, bg="#BC4CD0",bd=0)
button_add.place(x=380, y=3)

button_add_list = Button(root, image=icon1,command=add_list_button_click, bg="#BC4CD0",bd=0)
button_add_list.place(x=320, y=3)



def on_back_button():
    main_page()
    root3.withdraw()
    root.deiconify()

def on_save_button():
    response = messagebox.showinfo("Save", "The note has been saved.")
    t=TextNote()
    if(len(textbox4.get("1.0",END).strip())==0 ):
        a="New Note"
    else:
        a=textbox4.get("1.0",END).strip()
    t.add_note(a,"text",textbox3.get("1.0",END).strip())
    main_page()

def add_page():
    button3 = Button(root3, text="BACK",command=on_back_button, fg="green", font=("Inter", 10, "bold"), bg="white", bd=0)
    button3.place(x=10, y=15)

    button_save = Button(root3, text="SAVE",command=on_save_button, bg="#BC4CD0",fg="white", bd=0,font=("Arial", 10, "bold"),width=10,height=1,highlightthickness=3, highlightbackground="gray")
    button_save.place(x=180, y=580)


def main_page():

    for widget in second_frame.winfo_children():
        widget.destroy()
    second_frame.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

    notess = get_all_notes()
    for i in notess:
        new_canvas = Canvas(second_frame, width=420, height=100, bg="#FCD2F4", bd=2, highlightthickness=2,
                            highlightbackground="grey")
        new_canvas.pack(pady=5)
        label = Label(new_canvas, text=((i[1][:20] + "...").replace("\n"," ") if len(i[1])>20 else i[1][:20].replace("\n"," ")), bg="#FCD2F4", fg="black", font=("Inter", 14))
        label.place(x=20, y=40)
        label = Label(new_canvas, text=((i[3][:20] + "...").replace("\n"," ") if len(i[3])>20 else i[3][:20].replace("\n"," ")), bg="#FCD2F4", fg="grey", font=("Inter", 10))
        label.place(x=20, y=70)
        button = Button(new_canvas, image=icon2, command=lambda note_id=i[0]: handle_button_click(note_id),
                        bg="#FCD2F4", bd=0)
        button.place(x=350, y=20)
        label = Label(new_canvas, text=i[2].upper(), bg="#FCD2F4", fg="#BC4CD0", font=("Inter", 10))
        label.place(x=10, y=8)


def handle_save_button(t):
    response = messagebox.showinfo("Save", "The note has been saved.")
    t.title = textbox2.get("1.0", END).strip()
    t.content = textbox1.get("1.0", END).strip()
    t.type = NoteType.TEXT.value.strip()

    t.update_note(t.note_id, t.title, NoteType.TEXT.value.strip(), t.content)

def handle_back_button():
        main_page()
        root.deiconify()
        root2.withdraw()


def handle_delete_button(x):
    raspuns = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the note?")
    if raspuns:
        t = TextNote()
        t.delete_note(x)
        response=messagebox.showinfo("Confirm Delete", "The note has been deleted.")
        if response is None:
            print("The OK button was pressed.")
        else:
            main_page()
            root.deiconify()
            root2.withdraw()
    else:
        pass

def handle_delete_list_button(x):
    itemss.clear()
    items.clear()
    raspuns = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the note?")
    if raspuns:
        t =  ListNote()
        t.delete_note(x)
        response = messagebox.showinfo("Confirm Delete", "The note has been deleted.")
        if response is None:
            print("The OK button was pressed.")
        else:
            main_page()
            root.deiconify()
            root5.withdraw()
            textbox6.delete("1.0", END)
            for widget in canvasq_frame.winfo_children():
                widget.destroy()
            canvasq_frame.configure(background="#FCD2F4")
            canvasq.config(scrollregion=canvasq.bbox("all"))
            main_page()
            itemss.clear()
            items.clear()
    else:
        pass
    itemss.clear()

def  handle_save_list_button(t):
        elements = []
        for i in itemss:
            elements.append({i["text"]: i["checked"]})
        l = ListNote()
        x=textbox6.get("1.0", END).strip() if len(textbox6.get("1.0", END).strip()) > 0 else "New Note"
        l.update_note(t,x,elements)
        messagebox.showinfo("Save", "The note has been saved.")

def handle_button_click(id):
   items.clear()
   if(check_note_type(id)=="text"):
    t=TextNote()
    root2.deiconify()
    root.withdraw()

    textbox2.delete("1.0", END)
    textbox1.delete("1.0", END)
    textbox2.insert("1.0", t.get_note(id)[1])
    textbox2.place(x=80, y=80)
    textbox1.insert("1.0",t.get_note(id)[3])
    new_note=TextNote()
    new_note.title=textbox2.get("1.0",END).strip()
    new_note.content=textbox1.get("1.0",END).strip()
    new_note.type=NoteType.TEXT.value.strip()
    new_note.note_id=id
    button_save = Button(root2, text="SAVE",command=lambda t=new_note: handle_save_button(t), bg="#BC4CD0", fg="white", bd=0, font=("Arial", 10, "bold"), width=10,
                         height=1, highlightthickness=3, highlightbackground="gray")
    button_save.place(x=180, y=580)
    button = Button(root2, text="BACK",command=handle_back_button, fg="green", font=("Inter", 10, "bold"), bg="white", bd=0)
    button.place(x=10, y=15)
    button2 = Button(root2, text="DELETE", command=lambda x=id:handle_delete_button(x), fg="red", font=("Inter", 10, "bold"),bg="white", bd=0)
    button2.place(x=80, y=15)
   else:
       itemss.clear()

       root5.deiconify()
       root.withdraw()
       l = ListNote()
       c = l.get_note(id)
       try:
        textbox6.insert("1.0", c[0][5] if len(c[0][5])>0 else " " )
       except Exception as e:
           pass
       nn=[]
       for i in c:
           nn.append({i[2]:i[3]})
       for i in nn:
           for j in i:
               add_item2(j,i[j])
       button3 = Button(root5, text="BACK", command=on_back_list, fg="green", font=("Inter", 10, "bold"), bg="white",
                        bd=0)
       button3.place(x=10, y=15)
       button2 = Button(root5, text="DELETE", command=lambda x=id: handle_delete_list_button(x), fg="red",
                        font=("Inter", 10, "bold"), bg="white", bd=0)
       button2.place(x=80, y=15)
       t=id
       button_save = Button(root5, text="SAVE", command=lambda : handle_save_list_button(id), bg="#BC4CD0",
                            fg="white", bd=0, font=("Arial", 10, "bold"), width=10,
                            height=1, highlightthickness=3, highlightbackground="gray")
       button_save.place(x=180, y=580)


if __name__=="__main__":
 create_tables()
 main_page()
 root.mainloop()
