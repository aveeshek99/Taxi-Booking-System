from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from Booking import Book
from BookingManager import insert,search,delete
from PIL import ImageTk,Image

class book():
    def __init__(self):
        #Function for confirming Booking:
        def conf():
            pickup = txtPick.get()
            dropoff = txtDrop.get()
            date = txtDate.get()
            payment = txtPay.get()
            nb1 = Book(pickup,dropoff,date,payment)
            result = insert(nb1)
            if result==True:
                messagebox.showinfo("Result","Booking Confirmed")
            else:
                messagebox.showerror("Result","Error")
        #Function for Cancelling Boooking:
        def canc():
            pick = txtPick.get()
            drop = txtDrop.get()
            result = delete(pick,drop)
            if result == True:
                messagebox.showinfo("Result","Booking Cancelled")
            else:
                messagebox.showerror("Result","Error")
        #Function for logging out:
        def logout():
            root.destroy()
            from CLogin import main
            main.__init__(self) 
        #Main Window Intialization(GUI):
        root = Tk()
        root.title("Booking")
        root.geometry("650x500")
        root.resizable(False,False)
        variable = StringVar(root)

        #Image:
        bg_frame = Image.open("inside3.jpg")
        photo = ImageTk.PhotoImage(bg_frame, master=root)
        bg_panel = Label(root, image=photo)
        bg_panel.image = photo
        bg_panel.pack(fill='both', expand='yes')

        #Heading:
        lbl_heading = Label(root,text="BOOKING", font=("Elephant",15,"bold"),bg="white").place(x=250,y=10)

        #Body:
        lblPick = Label(root,text = "PICKUP LOCATION :")
        txtPick = Entry(root,width=20)
        lblPick.place(x=20,y=50)
        txtPick.place(x=135,y=50)


        lblDrop = Label(root,text = "DESTINATION :")
        txtDrop = Entry(root,width=20)
        lblDrop.place(x=275,y=50)
        txtDrop.place(x=365,y=50)

        lblDate = Label(root,text="DATE :")
        txtDate = DateEntry(root, width=12, year=2023, month=1, day=1, 
        background='darkblue', foreground='white', borderwidth=2)
        lblDate.place(x=500,y=50)
        txtDate.place(x=545,y=50)

        lblPay = Label(root, text="PAYMENT METHOD:")
        txtPay = ttk.Combobox(state="readonly",values=["Cash","Mobile Banking","E-sewa","Khalti"])
        lblPay.place(x=10,y=80)
        txtPay.place(x=130,y=80)

        #Table Design:
        frame1 = Frame(root)
        frame1.place(x=40,y=150)

        tblPersons = ttk.Treeview(frame1)
        tblPersons['columns'] = ('bid','pick','drop','date','pay')

        tblPersons.column("#0",width=0,stretch=NO)
        tblPersons.column("bid",width=50,anchor=CENTER)
        tblPersons.column("pick",width=150,anchor=CENTER)
        tblPersons.column("drop",width=150,anchor=CENTER)
        tblPersons.column("date",width=100,anchor=CENTER)
        tblPersons.column("pay",width=100,anchor=CENTER)

        tblPersons.heading("#0",text="",anchor=CENTER)
        tblPersons.heading("bid",text="ID",anchor=CENTER)
        tblPersons.heading("pick",text="PICKUP",anchor=CENTER)
        tblPersons.heading("drop",text="DROPOFF",anchor=CENTER)
        tblPersons.heading("date",text="DATE",anchor=CENTER)
        tblPersons.heading("pay",text="PAYMENT",anchor=CENTER)

        #Function for viewing and inserting data in table:
        def view():
            pick = txtPick.get()
            drop = txtDrop.get()
            trips = search(pick,drop)
            for trip in trips:
                tblPersons.insert(parent='', index='end',iid=trip[0], values=(trip[0],trip[1],trip[2],trip[3],trip[4]))

        tblPersons.pack()

        #Buttons:
        btnMake = Button(root,text="MAKE BOOKING",command=conf)
        btnMake.place(x=280,y=80)
        btnView = Button(root,text="VIEW BOOKING",command = view)
        btnView.place(x=400,y=80)
        btnCan = Button(root,text="CANCEL BOOKING",command = canc)
        btnCan.place(x=520,y=80)
        btnLog = Button(root,text="LOGOUT",command=logout)
        btnLog.place(x=280,y=400)
        root.mainloop()