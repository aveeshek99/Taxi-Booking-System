from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
from DriverManager import search
from PIL import ImageTk,Image

class Drivebook():
    def __init__(self):
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
        lbl_heading = Label(root,text="BOOKING INFO", font=("Elephant",15,"bold"),bg="white").place(x=200,y=10)

        #Table Design:
        frame1 = Frame(root)
        frame1.place(x=40,y=100)

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
        tblPersons.heading("pick",text="NAME",anchor=CENTER)
        tblPersons.heading("drop",text="ADDRESS",anchor=CENTER)
        tblPersons.heading("date",text="DATE",anchor=CENTER)
        tblPersons.heading("pay",text="PAYMENT",anchor=CENTER)

        #Function for viewing and inserting info in table:
        def view():
            trips = search()
            for trip in trips:
                tblPersons.insert(parent='', index='end',iid=trip[0], values=(trip[0],trip[1],trip[2],trip[3],trip[4]))

        tblPersons.pack()
        
        #Buttons:
        btnView = Button(root,text="VIEW BOOKING",command=view)
        btnView.place(x=125,y=350)

        btnLog = Button(root,text="LOGOUT",command=logout)
        btnLog.place(x=380,y=350)
        root.mainloop()