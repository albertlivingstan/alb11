from tkinter import *
from tkinter import ttk
import sqlite3

class Student:
    def __init__(self, tk):
        self.tk = tk
        self.create_database()
        self.create_gui()

    def create_database(self):
        c = sqlite3.connect("Student.db")
        curs = c.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS Student(ID INTEGER PRIMARY KEY, NAME VARCHAR(20), AGE INTEGER, DOB VARCHAR(20), GENDER VARCHAR(20), CITY VARCHAR(20))")
        c.commit()
        c.close()
        print("Table created")

    def create_gui(self):
        self.T_Frame = Frame(self.tk, height=50, width=1200, bg="blue", bd=2, relief=GROOVE)
        self.T_Frame.pack()
        self.Title = Label(self.T_Frame, text="Student Management System", font="arial 20 bold", width=1200, bg="blue")
        self.Title.pack()

        # frame work 1
        self.Frame_1 = Frame(self.tk, height=580, width=400, bd=2, relief=GROOVE, bg="blue")
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)

        # label work 1
        Label(self.Frame_1, text="Student Details", bg="blue", font="arial 12 bold").place(x=20, y=20)

        # id work

        
        self.Id = Label(self.Frame_1, text="Id", bg="blue", font="arial 10 bold")
        self.Id.place(x=50, y=60)
        self.Id_Entry = Entry(self.Frame_1, width=40)
        self.Id_Entry.place(x=150, y=60)

        self.Name = Label(self.Frame_1, text="Name", bg="blue", font="arial 10 bold")
        self.Name.place(x=40, y=100)
        self.Name_Entry = Entry(self.Frame_1, width=40)
        self.Name_Entry.place(x=150, y=100)

        self.Age = Label(self.Frame_1, text=" Age ", bg="blue", font="arial 10 bold")
        self.Age.place(x=40, y=140)
        self.Age_Entry = Entry(self.Frame_1, width=40)
        self.Age_Entry.place(x=150, y=140)

        self.DOB = Label(self.Frame_1, text="DOB", bg="blue", font="arial 10 bold")
        self.DOB.place(x=40, y=180)
        self.DOB_Entry = Entry(self.Frame_1, width=40)
        self.DOB_Entry.place(x=150, y=180)

        self.Gender = Label(self.Frame_1, text="Gender", bg="blue", font="arial 10 bold")
        self.Gender.place(x=40, y=220)
        self.Gender_Entry = Entry(self.Frame_1, width=40)
        self.Gender_Entry.place(x=150, y=220)

        self.City = Label(self.Frame_1, text="City", bg="blue", font="arial 10 bold")
        self.City.place(x=40, y=260)
        self.City_Entry = Entry(self.Frame_1, width=40)
        self.City_Entry.place(x=150, y=260)

        # BUTTONS frame work
        self.Button_Frame = Frame(self.Frame_1, height=350, width=450, relief=GROOVE, bd=2, bg="blue")
        self.Button_Frame.place(x=100, y=380)

        # =====BUTTONS====
        self.Add = Button(self.Button_Frame, text="Add", width=25, font="arial 11 bold", command=self.Add)
        self.Add.pack()
        self.Delete = Button(self.Button_Frame, text="Delete", width=25, font="arial 11 bold", command=self.Delete)
        self.Delete.pack()
        self.Update = Button(self.Button_Frame, text="Update", width=25, font="arial 11 bold", command=self.Update)
        self.Update.pack()
        self.Clear = Button(self.Button_Frame, text="Clear", width=25, font="arial 11 bold", command=self.Clear)
        self.Clear.pack()

        # frame_1 finished
        
        # frame work 2
        self.Frame_2 = Frame(self.tk, height=580, width=800, bd=2, relief=GROOVE, bg="white")
        self.Frame_2.pack(side=RIGHT)

        # table work
        self.tree = ttk.Treeview(self.Frame_2, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings", height=25)
        self.tree.pack()
        self.tree.column("#1", anchor=CENTER, width=100)
        self.tree.heading("#1", text="ID")
        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="Name")
        self.tree.column("#3", anchor=CENTER, width=115)
        self.tree.heading("#3", text="Age")
        self.tree.column("#4", anchor=CENTER, width=110)
        self.tree.heading("#4", text="DOB")
        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="Gender")
        self.tree.column("#6", anchor=CENTER, width=110)
        self.tree.heading("#6", text="City")
        self.tree.insert("", index=0, values=(1, "vijay", 18, "12-2-2002", "male", 18, "chennai"))
        self.tree.pack()

    def Add(self):
        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        self.tree.insert("", index=0, values=(id, name, age, dob, gender, city))
        
        # using sqlite3
        c = sqlite3.connect("Student.db")
        curs = c.cursor()
        curs.execute("INSERT INTO Student (ID, NAME, AGE, DOB, GENDER, CITY) VALUES(?,?,?,?,?,?)", (id, name, age, dob, gender, city))
        c.commit()
        c.close()
        print("Value Inserted")

    def Delete(self):
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        print(selected_item)
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("DELETE FROM Student WHERE ID=?", (selected_item,))
        print("Value Deleted")
        c.commit()
        c.close()
        self.tree.delete(item)

    def Update(self):
        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        item = self.tree.selection()[0]
        self.tree.item(item, values=(id, name, age, dob, gender, city))
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("UPDATE Student SET NAME=?, AGE=?, DOB=?, GENDER=?, CITY=? WHERE ID=?", (name, age, dob, gender, city, id))
        c.commit()
        c.close()
        print("Value Updated")

    def Clear(self):
        self.Id_Entry.delete(0, END)
        self.Name_Entry.delete(0, END)
        self.Age_Entry.delete(0, END)
        self.DOB_Entry.delete(0, END)
        self.Gender_Entry.delete(0, END)
        self.City_Entry.delete(0, END)
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("UPDATE Student SET ID=?, NAME=?, AGE=?, DOB=?, GENDER=?, CITY=? WHERE ID=?", (selected_item, "", "", "", "", "", selected_item))
        c.commit()
        c.close()
        print("Values Updated")
        self.tree.item(item, values=(None, None, None, None, None, None))

tk = Tk()
tk.title("Student Management System")
tk.resizable(False, False)
tk.geometry("1200x600")

student_system = Student(tk)

tk.mainloop()
