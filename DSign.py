from tkinter import messagebox
from tkinter import *
from PIL import ImageTk,Image
from Driver import drive
from DriverManager import insert
import sys

class Sign2():
    def __init__(self):
        #Function for registering Driver:
        def save():
            name = txtName.get()
            addr = txtAdd.get()
            email = txtEmail.get()
            numb = txtNum.get()
            paswo = txtPas.get()
            repas = txtPass2.get()
            lice = txtLic.get()
            nb1 = drive(name,email,addr,numb,lice,paswo)
            result = insert(nb1)
            #Validation:
            if result==True and len(numb)==10 and len(paswo)>=8 and paswo==repas:
                messagebox.showinfo("Result","Driver Added")
                root.destroy()
                from CLogin import main
                main.__init__(self) 
            elif len(numb)<10 or len(numb)>10:
                messagebox.showerror("Result","Invalid Number")
            elif len(paswo)<8:
                messagebox.showerror("Result","Password must be at least 8 characters long.")
            elif paswo!=repas:
                messagebox.showerror("Result","Password doesn't match")
            else:
                messagebox.showerror("Result","Error")
                
        #Function for showing password:  
        def show():
            if txtPas.cget('show') == "*":
                txtPas.config(show='')
                txtPass2.config(show='')
            else:
                txtPas.config(show='*')
                txtPass2.config(show='*')
        #Function for logging out:
        def close():
            root.destroy()
            from CLogin import main
            main.__init__(self) 

        #Main Window Intialization(GUI):
        root = Tk()
        root.title("Signup")
        root.geometry("360x450")
        root.resizable(False,False)

        bg_frame = Image.open("login_page.jpg")
        photo = ImageTk.PhotoImage(bg_frame, master=root)
        bg_panel = Label(root, image=photo)
        bg_panel.image = photo
        bg_panel.pack(fill='both', expand='yes')

        #Heading:
        lbl_heading = Label(root,text="DRIVER REGISTRATION", font=("Elephant",15,"bold"),bg="white").place(x=20,y=50)

        #Body:
        lblName = Label(root,text="NAME :")
        txtName = Entry(root,width=20)
        lblName.place(x=20,y=120)
        txtName.place(x=100,y=120)

        lblAdd = Label(root,text="ADDRESS :")
        txtAdd = Entry(root,width=20)
        lblAdd.place(x=20,y=150)
        txtAdd.place(x=100,y=150)

        lblEmail = Label(root,text="E-Mail :")
        txtEmail = Entry(root,width=20)
        lblEmail.place(x=20,y=180)
        txtEmail.place(x=100,y=180)

        lblNum = Label(root,text="MOBILE N0 :")
        txtNum= Entry(root,width=20)
        lblNum.place(x=20,y=210)
        txtNum.place(x=100,y=210)

        lblLic = Label(root,text="LICENSE NO :")
        txtLic = Entry(root,width=20)
        lblLic.place(x=20,y=240)
        txtLic.place(x=100,y=240)

        lblPas = Label(root,text="PASSWORD :")
        txtPas = Entry(root,show="*",width=20)
        lblPas.place(x=20,y=270)
        txtPas.place(x=100,y=270)

        lblPass2 = Label(root,text = "RE-PASSWORD :")
        txtPass2 = Entry(root,show="*",width=20)
        lblPass2.place(x=20,y=300)
        txtPass2.place(x=120,y=300)

        #Buttons:
        checkbtn = Checkbutton(root,text="Show Password",command=show)
        checkbtn.place(x=20,y=330)

        btnSign = Button(root,text="SIGN IN",command=save)
        btnCan = Button(root,text="CANCEL",command=close)
        btnSign.place(x=100,y=370)
        btnCan.place(x=200,y=370)

        root.mainloop()