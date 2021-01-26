from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import time
import random
import pyodbc


screen=Tk()
screen.title("THE HOTEL GRAND")
screen.config(bg='white')
screen.geometry('1024x751')

#Backgroud Image
bg = ImageTk.PhotoImage(file="bg.jpg")
#Background Image label
bg_label=Label(screen,image=bg)
bg_label.place(x=0,y=0, relwidth=1, relheight=1)

# Title label
title_label = Label(screen, text=" THE HOTEL GRAND ", height=2,bg='#000324',fg="Gold",font=('Brush Script MT', 30,'italic','underline','bold'))
title_label.pack()

# Welcome label
welcome_label = Label(screen, text=" WELCOME ", fg="Gold",bg="#000324", font=('Brush Script MT', 30,'italic','underline','bold'))
welcome_label.pack()

# Fuctions
def check_in():
    m = Toplevel(screen)
    m.title("Hotel Management System")
    m.geometry("1350x700")
    m.config(bg="#407ee3")
    guestref = StringVar()
    datein = StringVar()
    dateout = StringVar()

    datein.set(time.strftime("%d/%m/%Y"))
    dateout.set(time.strftime("%d/%m/%Y"))

    x = random.randint(100, 500)
    ranref = str(x)
    guestref.set(ranref)

    def exit1():
        exit1 = messagebox.askyesno("The Hotel Grand", "Do you want to leave?")
        # here 1 means ok or yes:
        if exit1 == 1:
            m.destroy()

    main_f = Frame(m)
    main_f.grid()

    def View():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\sample.accdb;'))
        cursor1 = con.cursor()
        cursor1.execute("select * from CUSTOMERDETAILS ORDER by CustomerID")
        rows = cursor1.fetchall()
        if len(rows) != 0:
            for i in rows:
                tree.insert('', END, values=i)
        con.close()

    def checkin():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\sample.accdb;'))
        cursor1 = con.cursor()

        cursor1.execute(
            f"INSERT INTO CUSTOMERDETAILS(CustomerID,FirstName,LastName,RoomType,LivesIn) values('{ID_e.get()}','{first_name_e.get()}','{last_name_e.get()}','{room_type_c.get()}','{live_in_e.get()}')")
        con.commit()
        View()
        messagebox.askyesno("The Hotel Grand","Do You Want To CHECK IN")
        con.close()
    def checkout():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\sample.accdb;'))
        cursor1 = con.cursor()
        cursor1.execute(f"DELETE FROM CUSTOMERDETAILS where CustomerID = {ID_e.get()}")
        con.commit()
        View()
        messagebox.askyesno("The Hotel Grand","One Record Has Been Deleted")
        con.close()

    def update():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\sample.accdb;'))
        cursor1 = con.cursor()
        cursor1.execute(f"UPDATE CUSTOMERDETAILS set LivesIn='{live_in_e.get()}' WHERE CustomerID={ID_e.get()}")
        con.commit()
        View()
        messagebox.askyesno("The Hotel Grand","Do Want To Update Existing Details")
        con.close()

    top_f = Frame(main_f, bd=10, width=1400, height=550, padx=55.5, relief=RIDGE, bg="#407ee3")
    top_f.pack(side=TOP)

    left_f = Frame(top_f, bd=7, width=400, height=600,relief=RIDGE, bg="#407ee3")
    left_f.pack(side=LEFT)

    right_f = Frame(top_f, bd=5, width=820, height=600, relief=RIDGE)
    right_f.pack(side=RIGHT)

    right_f1 = Frame(right_f, bd=5, width=800, height=600, relief=RIDGE)
    right_f1.pack()
    right_f2 = Frame(right_f, bd=5, width=800, height=600, relief=RIDGE)
    right_f2.pack(pady=180)

    bottom_f = Frame(main_f, bd=10, width=1000, height=120, padx=6, relief=RIDGE, bg="#407ee3")
    bottom_f.pack(side=BOTTOM, fill=BOTH)

    hotel_name = Label(left_f,text=" THE HOTEL GRAND ",font=('Brush Script MT',14,'italic','underline','bold'),
                       fg="gold", bg="white", bd=14, relief=RIDGE)
    hotel_name.grid()

    guest_ref = Label(left_f,font=('Brush Script MT',14,'italic','underline','bold'), text="Guest Reference Number", padx=1,bg="#407ee3")
    guest_ref.grid(row=1, column=0)
    guest_ref_e = Entry(left_f, font=('Brush Script MT',14,'italic','underline','bold'), width=18, textvariable=guestref)
    guest_ref_e.grid(row=1, column=1,padx=3, pady=25)

    ID = Label(left_f,font=('Brush Script MT',14,'italic','underline','bold'), text="ID", padx=1,bg="#407ee3")
    ID.grid(row=2, column=0)
    ID_e = Entry(left_f,font=('Brush Script MT',14,'italic','underline','bold'), width=18)
    ID_e.grid(row=2, column=1, padx=3, pady=25)

    first_name = Label(left_f,font=('Brush Script MT',14,'italic','underline','bold'), text="FIRST NAME", padx=1,bg="#407ee3")
    first_name.grid(row=3, column=0)
    first_name_e = Entry(left_f,font=('Brush Script MT',14,'italic','underline','bold'), width=18)
    first_name_e.grid(row=3, column=1, padx=3, pady=25)

    last_name = Label(left_f,font=('Brush Script MT',14,'italic','underline','bold'), text="LAST NAME", padx=1,bg="#407ee3")
    last_name.grid(row=4, column=0)
    last_name_e = Entry(left_f,font=('Brush Script MT',14,'italic','underline','bold'), width=18)
    last_name_e.grid(row=4, column=1, padx=3, pady=25)

    live_in = Label(left_f,font=('Brush Script MT',14,'italic','underline','bold'), text="LIVES IN", padx=1,bg="#407ee3")
    live_in.grid(row=5, column=0)
    live_in_e = Entry(left_f, font=('Brush Script MT',14,'italic','underline','bold'), width=18)
    live_in_e.grid(row=5, column=1, padx=3, pady=25)

    room_type = Label(left_f,font=('Brush Script MT',14,'italic','underline','bold'), text="Room Type", padx=1,bg="#407ee3")
    room_type.grid(row=6, column=0)
    rooms = ["Single", "Deluxe", "Royale"]
    room_type_c = ttk.Combobox(left_f, values=rooms, state='readonly',font=('Brush Script MT', 14,'italic','underline','bold'), width=16)
    room_type_c.set("Pick A Room Type")
    room_type_c.grid(row=6, column=1, padx=3, pady=25)

    check_in = Label(left_f, font=('Brush Script MT', 14, 'italic', 'underline', 'bold'), text="Check In date", padx=1, bg="#407ee3")
    check_in.grid(row=7, column=0)
    check_in_e = Entry(left_f,font=('Brush Script MT', 14,'italic','underline','bold'),width=18, textvariable=datein)
    check_in_e.grid(row=7, column=1, padx=3,pady=20)

    check_out = Label(left_f,font=('Brush Script MT', 14,'italic','underline','bold'),text="Check Out date", padx=1,bg="#407ee3")
    check_out.grid(row=8, column=0)
    check_out_e = Entry(left_f,font=('Brush Script MT', 14,'italic','underline','bold'), width=18, textvariable=dateout)
    check_out_e.grid(row=8, column=1,padx=3, pady=20)

    l1 = Label(right_f1,font=('Brush Script MT', 12,'italic','underline','bold'), padx=6, pady=10,
               text="DETAILS SECTION")
    l1.grid(row=0, column=0)

    #second window buttons:
    update_but = Button(bottom_f, bd=4, width=14, height=1, text="Update",font=('Brush Script MT',23,'italic','underline','bold'),command=update)
    update_but.grid(row=0, column=0, padx=50, pady=15)

    checkin_but = Button(bottom_f, bd=4, width=10, height=1, text="Check In",
    font=('Brush Script MT',23,'italic','underline','bold'),command=checkin)
    checkin_but.grid(row=0, column=3, padx=50, pady=15)

    checkout_but = Button(bottom_f, bd=4, width=10, height=1, text="Check Out",
    font=('Brush Script MT',23,'italic','underline','bold'),command=checkout)
    checkout_but.grid(row=0, column=4, padx=50, pady=15)

    cust_but = Button(bottom_f, bd=4, width=16, height=1, text="Customer Details",
     font=('Brush Script MT',23,'italic','underline','bold'),command=View)
    cust_but.grid(row=0, column=5, padx=50, pady=15)

    exit_but = Button(bottom_f, bd=4, width=10, height=1, text="Exit", command=exit1,
    font=('Brush Script MT',23,'italic','underline','bold'))
    exit_but.grid(row=0, column=6, padx=50, pady=15)

    # here tree is variable of the function treeview:

    tree = ttk.Treeview(right_f2, column=("column1", "column2", "column3", "column4","column5"), show='headings')

    tree.heading("#1", text="ID")

    tree.heading("#2", text="FIRST NAME")

    tree.heading("#3", text="LAST NAME")

    tree.heading("#4", text="ROOM TYPE")

    tree.heading("#5", text="LIVES IN")

    tree.pack()

# Buttons
Proceed_button = Button(screen, text="Proceed", fg='black',bg="#fcd305", font=('Brush Script MT', 20, 'bold','italic'), width=20,
                    command=check_in)
Proceed_button.pack(pady=70)
exit_button = Button(screen, text="Exit", fg="black", width=20,bg="#fcd305",font=('Brush Script MT', 20, 'bold','italic'), command=screen.quit)
exit_button.pack(pady=70)


screen.mainloop()