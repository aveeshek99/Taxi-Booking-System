from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from PasswordManager import edit

class passwo():
    def __init__(self):
        #Function for showing password:
        def show():
            if txtPass.cget('show') == "*":
                txtPass.config(show='')
                txtPass2.config(show='')
            else:
                txtPass.config(show='*')
                txtPass2.config(show='*')
        #Function for editing password:
        def conf():
            pas1 = txtPass.get()
            pas2 = txtPass2.get()
            result = edit(pas1,txtUser.get())
            #Validation:
            if pas1 == pas2 and result==True and len(pas1)>=8:
                messagebox.showinfo("Result","Password Reset")
                root.destroy()
                from CLogin import main
                main.__init__(self) 
            elif pas1!=pas2:
                messagebox.showerror("Result","Password doesn't match")
            elif len(pas1)<8:
                messagebox.showerror("Result","Password must be at least 8 characters long")
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
        lbl_heading = Label(root,text="New Password", font=("Elephant",15,"bold"),bg="white").place(x=100,y=50)

        #Body:
        lblUser = Label(root,text = "Username/E-mail :")
        txtUser = Entry(root,width=20)
        lblUser.place(x=70,y=200)
        txtUser.place(x=200,y=200)


        lblPass = Label(root,text = "Password :")
        txtPass = Entry(root,show="*",width=20)
        lblPass.place(x=70,y=250)
        txtPass.place(x=200,y=250)

        lblPass2 = Label(root,text = "Confirm Password :")
        txtPass2 = Entry(root,show="*",width=20)
        lblPass2.place(x=70,y=300)
        txtPass2.place(x=200,y=300)

        #Buttons:
        checkbtn = Checkbutton(root,text="Show Password",command=show)
        checkbtn.place(x=120,y=340)

        btnCon = Button(root,text="CONFIRM",command=conf)
        btnCon.place(x=70,y=370)

        btnCan = Button(root,text="CANCEL",command=close)
        btnCan.place(x=200,y=370)

        root.mainloop()