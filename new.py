from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import time
import random
import datetime
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
title_label = Label(screen, text=" THE HOTEL GRAND ", height=2,bg='#000324',fg="white",font=('Brush Script MT', 30,'italic','underline','bold'))
title_label.pack()

# Welcome label
welcome_label = Label(screen, text=" WELCOME ", fg="white",bg="#000324", font=('Brush Script MT', 30,'italic','underline','bold'))
welcome_label.pack()

# Fuctions
def check_in():
    m = Toplevel(screen)
    m.title("Hotel Management System")
    m.geometry("1350x700")
    m.config(bg="#407ee3")
    guestref = StringVar()
    firstname = StringVar()
    lastname = StringVar()
    email = StringVar()
    datein = StringVar()
    dateout = StringVar()
    roomno = StringVar()
    roomtype = StringVar()
    dayno = StringVar()
    tax = StringVar()
    subtotal = StringVar()
    total = StringVar()

    datein.set(time.strftime("%d/%m/%Y"))
    dateout.set(time.strftime("%d/%m/%Y"))

    x = random.randint(1000, 5000)
    ranref = str(x)
    guestref.set(ranref)

    def exit1():
        exit1 = messagebox.askyesno("Hotel California", "Do you want to leave?")
        if exit1 > 0:
            m.destroy()

    main_f = Frame(m)
    main_f.grid()

    top_f = Frame(main_f, bd=10, width=1350, height=550, padx=2, relief=RIDGE, bg="#407ee3")
    top_f.pack(side=TOP)

    left_f = Frame(top_f, bd=7, width=400, height=600, relief=RIDGE, bg="#407ee3")
    left_f.pack(side=LEFT)

    right_f = Frame(top_f, bd=5, width=820, height=550, relief=RIDGE)
    right_f.pack(side=RIGHT)

    right_f1 = Frame(right_f, bd=5, width=800, height=50, padx=10, relief=RIDGE)
    right_f1.grid(row=0, column=0)
    right_f2 = Frame(right_f, bd=5, width=800, height=300, padx=3, relief=RIDGE)
    right_f2.grid(row=1, column=0)
    right_f3 = Frame(right_f, bd=5, width=800, height=300, padx=4, relief=RIDGE)
    right_f3.grid(row=3, column=0)

    bottom_f = Frame(main_f, bd=10, width=1000, height=120, padx=2, relief=RIDGE, bg="#407ee3")
    bottom_f.pack(side=BOTTOM, fill=BOTH)

    hotel_name = Label(left_f, text="The Hotel California", font=("algerian", 19, "bold"),
                       fg="gold", bg="black", bd=14, relief=RAISED)
    hotel_name.grid()

    # img = PhotoImage(file=r"C:\Users\ehtes\OneDrive\Documents\cali.png")
    # img1 = img.subsample(2, 2)
    # img2 = Label(left_f, image=img1).grid(row=0, column=1)

    guest_ref = Label(left_f, font=("arial", 12, "bold"), text="Guest Reference Number", padx=1, bg="powder blue")
    guest_ref.grid(row=1, column=0)
    guest_ref_e = Entry(left_f, font=("arial", 12, "bold"), width=18, textvariable=guestref).grid(row=1, column=1,
                                                                                                  padx=3, pady=25)

    first_name = Label(left_f, font=("arial", 12, "bold"), text="First Name", padx=1, bg="powder blue")
    first_name.grid(row=2, column=0)
    first_name_e = Entry(left_f, font=("arial", 12, "bold"), width=18).grid(row=2, column=1, padx=3, pady=25)

    last_name = Label(left_f, font=("arial", 12, "bold"), text="Last Name", padx=1, bg="powder blue")
    last_name.grid(row=3, column=0)
    last_name_e = Entry(left_f, font=("arial", 12, "bold"), width=18).grid(row=3, column=1, padx=3, pady=25)

    address = Label(left_f, font=("arial", 12, "bold"), text="Email Address", padx=1, bg="powder blue")
    address.grid(row=4, column=0)
    address_e = Entry(left_f, font=("arial", 12, "bold"), width=18).grid(row=4, column=1, padx=3, pady=25)

    room_type = Label(left_f, font=("arial", 12, "bold"), text="Room Type", padx=1, bg="powder blue")
    room_type.grid(row=6, column=0)
    types = ["Single", "Deluxe", "Royale"]
    room_type_c = ttk.Combobox(left_f, values=types, state='readonly', font=("arial", 12, "bold"), width=16)
    room_type_c.set("Pick a Room Type")
    room_type_c.grid(row=6, column=1, padx=3, pady=25)

    check_in = Label(left_f, font=("arial", 12, "bold"), text="Check In date", padx=1, bg="powder blue")
    check_in.grid(row=7, column=0)
    check_in_e = Entry(left_f, font=("arial", 12, "bold"), width=18, textvariable=datein).grid(row=7, column=1, padx=3,
                                                                                               pady=20)

    check_out = Label(left_f, font=("arial", 12, "bold"), text="Check Out date", padx=1, bg="powder blue")
    check_out.grid(row=8, column=0)
    check_out_e = Entry(left_f, font=("arial", 12, "bold"), width=18, textvariable=dateout).grid(row=8, column=1,
                                                                                                 padx=3, pady=20)

    l1 = Label(right_f1, font=("arial", 12, "bold"), padx=6, pady=10,
               text="Booking ID\tFirst Name\tLast Name\tCheck In\t    Check Out\tRoom Number").grid(row=0, column=0)

    tax = Label(right_f3, bd=3, relief=RIDGE, font=("arial", 14, "bold"), text="Paid Tax", padx=2, pady=2, bg="teal")
    tax.grid(row=1, column=0)
    tax_e = Entry(right_f3, font=("arial", 12, "bold"), width=25).grid(row=1, column=1, padx=3, pady=15)

    sub_total = Label(right_f3, bd=3, relief=RIDGE, font=("arial", 14, "bold"), text="Subtotal", padx=2, pady=2,
                      bg="teal")
    sub_total.grid(row=2, column=0)
    sub_total_e = Entry(right_f3, font=("arial", 14, "bold"), width=25).grid(row=2, column=1, padx=3, pady=15)

    total = Label(right_f3, bd=3, width=5, relief=RIDGE, font=("arial", 14, "bold"), text="Total", padx=2, pady=2,
                  bg="teal")
    total.grid(row=3, column=0)
    total_e = Entry(right_f3, font=("arial", 14, "bold"), width=25).grid(row=3, column=1, padx=3, pady=15)

    update_but = Button(bottom_f, bd=4, width=14, height=1, text="Update",
                        font=("arial", 18, "bold")).grid(row=0, column=0, padx=11, pady=15)

    room_but = Button(bottom_f, bd=4, width=14, height=1, text="Room Details",
                      font=("arial", 18, "bold")).grid(row=0, column=1, padx=11, pady=15)

    checkin_but = Button(bottom_f, bd=4, width=10, height=1, text="Check In",
                         font=("arial", 18, "bold")).grid(row=0, column=3, padx=11, pady=15)

    checkout_but = Button(bottom_f, bd=4, width=10, height=1, text="Check Out",
                          font=("arial", 18, "bold")).grid(row=0, column=4, padx=11, pady=15)

    cust_but = Button(bottom_f, bd=4, width=16, height=1, text="Customer Details",
                      font=("arial", 18, "bold")).grid(row=0, column=5, padx=11, pady=15)

    exit_but = Button(bottom_f, bd=4, width=10, height=1, text="Exit", command=exit1,
                      font=("arial", 18, "bold")).grid(row=0, column=6, padx=13, pady=15)


def check_out():
    checkout=Toplevel(screen)
    checkout.title("Check Out Window")
    checkout.grid()
def room_details():
    room=Toplevel(screen)
    room.title("Check In Window")
    room.grid()
def customer_detail():
    checkdetail=Toplevel(screen)
    checkdetail.title("Check In Window")
    checkdetail.grid()


# Buttons
check_in_button = Button(screen, text="Check In", fg='black', font=('Brush Script MT', 20, 'bold','italic'), width=30,
                    command=check_in)
check_in_button.pack(pady=10)
check_out_button = Button(screen, text="Check Out", fg='black', font=('Brush Script MT', 20, 'bold','italic'), width=30,
                    command=check_out)
check_out_button.pack(pady=10)
room_detail_button = Button(screen, text="Room Details", fg='black', font=('Brush Script MT', 20, 'bold','italic'), width=30,
                   command=room_details)
room_detail_button.pack(pady=10)
customer_detail_button = Button(screen, text="Customer Details", fg='black', font=('Brush Script MT', 20, 'bold','italic'),width=30,
                   command=customer_detail)
customer_detail_button.pack(pady=10)
exit_button = Button(screen, text="Exit", fg="black", width=30,font=('Brush Script MT', 20, 'bold','italic'), command=screen.quit)
exit_button.pack(pady=10)


screen.mainloop()