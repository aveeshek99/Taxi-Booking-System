from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
from AdminManager import allBooking,deleteBooking
from DriverList import Dlist
from PIL import ImageTk,Image

class admin():
    def __init__(self):
        
        #Function for assigning booking to Driver
        def assign():
            root.destroy()
            Dlist()

        #Main Window Intialization(GUI):
        root = Tk()
        root.title("Booking")
        root.geometry("650x500")
        root.resizable(False,False)
        variable = StringVar(root)
        tripId = None

        #Image:
        # bg_frame = Image.open("taxi1.jpg")
        bg_frame = Image.open("inside3.jpg")
        photo = ImageTk.PhotoImage(bg_frame, master=root)
        bg_panel = Label(root, image=photo)
        bg_panel.image = photo
        bg_panel.pack(fill='both', expand='yes')

        #Heading:
        lbl_heading = Label(root,text="BOOKING CONSOLE", font=("Elephant",15,"bold"),bg="white").place(x=200,y=10)

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

        #Function for selecting info in table:
        def selectID():
            tripId = tblPersons.selection()[0]
            return tripId
        tblPersons.bind("<<TreeviewSelect>>",selectID)

        #Function for viewing and inserting info in table:
        def view():
            trips = allBooking()
            for trip in trips:
                tblPersons.insert(parent='', index='end',iid=trip[0], values=(trip[0],trip[1],trip[2],trip[3],trip[4]))

        tblPersons.pack()

        #Buttons:
        btnView = Button(root,text="VIEW BOOKING",command=view)
        btnView.place(x=120,y=80)

        btnView = Button(root,text="ASSIGN BOOKING",command = assign)
        btnView.place(x=265,y=80)

        #Function for cancelling booking:
        def canc():
            id = selectID()
            result = deleteBooking(id)
            if result == True:
                messagebox.showinfo("Result","Booking Cancelled")
            else:
                messagebox.showerror("Result","Error")
        #Function for logging out:
        def logout():
            root.destroy()
            from CLogin import main
            main.__init__(self) 
        #Buttons:
        btnCan = Button(root,text="CANCEL BOOKING",command=canc)
        btnCan.place(x=420,y=80)

        btnLog = Button(root,text="LOGOUT",command= logout)
        btnLog.place(x=300,y=400)
        root.mainloop()