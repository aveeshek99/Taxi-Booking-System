from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from CSign import Sign1
from DSign import Sign2
from CPass import passwo
from CBook import book
from DBook import Drivebook
from AdminUi import admin
from LoginManager import search
import sys

class main():
    def __init__(self):
        #Function for login as customer,driver or admin:
        def log():
            mail = txtID.get()
            pas = txtPass.get()
            login = search(mail,pas)
            #Code for differentiating login as driver,customer or admin:
            if login == 1:
                root.destroy()
                book()
            elif login == 2:
                root.destroy()
                Drivebook()
            elif login == 3:
                messagebox.showinfo("Result","Welcome Super Admin")
                root.destroy()
                admin()
            else:
                messagebox.showerror("Result","Invalid Username")
        #Function to open window for customer registration: 
        def sign1():
            root.destroy()
            Sign1()

         #Function to open window for driver registration:
        def sign2():
            root.destroy()
            Sign2()

        #Function for Forgot Password Button:
        def repass(*args):
            root.destroy()
            passwo()

        #Function for Show Password Check Button:
        def show():
            if txtPass.cget('show') == "*":
                txtPass.config(show='')
            else:
                txtPass.config(show='*')

        # Function to exit GUI:
        def close():
            sys.exit()

        #Main Window Intialization(GUI):
        root = Tk()
        root.title("Login")
        root.geometry("360x450")
        root.resizable(False,False)

        #Image:
        bg_frame = Image.open("login_page.jpg")
        photo = ImageTk.PhotoImage(bg_frame, master=root)
        bg_panel = Label(root, image=photo)
        bg_panel.image = photo
        bg_panel.pack(fill='both', expand='yes')

        #Heading:
        lbl_heading = Label(root,text="LOGIN", font=("Elephant",15,"bold"),bg="white").place(x=125,y=50)

        #Body:
        lblID = Label(root,text = "Username/E-mail :")
        txtID = Entry(root,width=20)
        lblID.place(x=70,y=150)
        txtID.place(x=180,y=150)

        lblPass = Label(root,text = "Password :")
        txtPass = Entry(root,show="*",width=20)
        lblPass.place(x=70,y=200)
        txtPass.place(x=180,y=200)

        checkbtn = Checkbutton(root,text="Show Password",command=show)
        checkbtn.place(x=50,y=230)

        lblFor = Label(root,text="Forgot Password?",font=("Arial",10,'underline'))
        lblFor.place(x=220,y=230)
        lblFor.bind('<Button-1>',repass)

        #Buttons:
        btnSave = Button(root,text="LOGIN",command=log)
        btnClose = Button(root,text="CLOSE",command=close)
        btnSave.place(x=100,y=270)
        btnClose.place(x=200,y=270)

        lblSign = Label(root,text="Don't have an account?Sign Up Here!!!")
        lblSign.place(x=80,y=310)
        btnSign1 = Button(root,text="SIGNUP AS CUSTOMER",command=sign1)
        btnSign1.place(x=30,y=358)
        btnSign2 = Button(root,text="SIGNUP AS DRIVER",command=sign2)
        btnSign2.place(x=210,y=358)

        root.mainloop()
#Function for dispalying login page:
main()