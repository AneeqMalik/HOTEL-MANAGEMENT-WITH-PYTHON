from tkinter import *
from PIL import ImageTk


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
title_label = Label(screen, text=" THE HOTEL GRAND ", height=2,bg='#000324',fg="white",font=('Brush Script MT',40, 'underline'))
title_label.pack()

# Welcome label
welcome_label = Label(screen, text=" WELCOME ", fg="white",bg="#000324", font=('Brush Script MT',30,'italic','underline','bold'))
welcome_label.pack()

#Fuctions
def check_in():
    checkin=Toplevel(screen)
    checkin.title("Check In Window")
    checkin.grid()
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