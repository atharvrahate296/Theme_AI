# necessary imports
from tkinter import messagebox
from tkinter import ttk
from  tkinter import *
import otp_validation as ov
import model as m
import data as d
import re

def landing_page(event=None):
    # main landing page
    w1=Tk()

    # create  a main landing page Tkinter window
    w1.title("Theme AI\u2122")
    w1.geometry("550x450+500+150")
    w1.iconbitmap("assets/bot.ico")
    w1.config(bg="#3A3B3D")
    

    l=Label(w1,text="You Personalized AI Chatbot!",font=(" Montserrat",20,"bold"),bg="#3A3B3D",fg="white")
    l.pack()
    l.place(relx=0.5,rely=0.25,anchor=CENTER)

    button_login=Button(w1,text="LOGIN",relief=GROOVE,font=(" Montserrat",12,"italic"),fg="#E9F5F4",bg="#4F8CE5",height=2,width=15,borderwidth=2)
    button_login.pack()
    button_login.place(relx=0.3,rely=0.6,anchor=CENTER)
    
    button_signup=Button(w1,text="SIGN-UP",relief=GROOVE,font=(" Montserrat",12,"italic"),width=15,height=2,borderwidth=2,fg="#E9F5F4",bg="#4F8CE5")
    button_signup.pack()
    button_signup.place(relx=0.7,rely=0.6,anchor=CENTER)

    # Hover Effects on buttons
    def enter_lg(event):
        button_login.config(bg="#0067FF",borderwidth=4,width=14)
    def enter_sp(event):
        button_signup.config(bg="#0067FF",borderwidth=4,width=14)

    def leave_lg(event):
        button_login.config(bg="#4F8CE5",borderwidth=2,width=15)
    def leave_sp(event):
        button_signup.config(bg="#4F8CE5",borderwidth=2,width=15)

    # bind actions to buttons
    button_login.bind("<Enter>",enter_lg)
    button_signup.bind("<Enter>",enter_sp)

    button_login.bind("<Leave>",leave_lg)
    button_signup.bind("<Leave>",leave_sp)
    def enter_login_page(event):
        # w1.after(200,w1.destroy())
        login_page()
    def enter_signup_page(event):
        # w1.after(200,w1.destroy())
        signup_page()

    button_login.bind("<Button-1>",enter_login_page)
    button_signup.bind("<Button-1>",enter_signup_page)
    
    # footer
    footer = Label(w1, text="© 2024 All rights reserved", font=("Montserrat", 10), bg="#3A3B3D", fg="white")
    footer.pack(side=BOTTOM,fill=X,pady=15)

    #mainloop
    w1.mainloop()

def login_page(event=None):
    #Login window here
    #Login Screen
    w2=Toplevel()

    w2.title("Theme AI\u2122")
    w2.geometry("650x550+450+100")
    w2.iconbitmap("assets/bot.ico")
    w2.config(bg="#414244")
    # w2.resizable(False,False)

    l=Label(w2,text="Theme AI",font=("Montserrat",30,"bold"),bg="#414244",fg="white")
    l.pack(padx=10,pady=10)
    l.place(relx=0.5,rely=0.1,anchor=CENTER)

    l1=Label(w2,text="Enter Login Details",font=('Montserrat',20,'bold'),bg="#414244",fg="white")
    l1.pack(padx=10,pady=10)
    l1.place(relx=0.3,rely=0.25,anchor=N)

    def enter_signup_page(event=None):
        w2.after(500,w2.destroy())
        signup_page()

    canvas=Canvas(w2,width=65,height=50,highlightthickness=0,bg="#414244")
    canvas.pack()
    canvas.place(relx=0.01)
    back=canvas.create_text(30,28,text="SIGNUP",fill="white",font=("Cambria",12,"underline"))
    canvas.tag_bind(back, "<Button-1>", enter_signup_page)

    #frame for login screen
    frame=Frame(w2,bg='#5B8DC0',width=500,height=310,relief=RIDGE,borderwidth=8)
    frame.pack(padx=20,pady=20)
    frame.place(relx=0.5,rely=0.35,anchor=N)

    #inside frame widgets :-
    #email entry
    l3=Label(frame,text="Enter Email : ",font=('Montserrat',18,'bold'),bg='#5B8DC0')
    l3.pack(padx=20,pady=40)
    l3.place(relx=0.1,rely=0.15)

    email=Entry(frame,width=25,bg="white",relief=GROOVE,borderwidth=5,font=('Cambria',12))
    email.pack(padx=20,pady=40)
    email.place(relx=0.18,rely=0.3)

    
    #password entry
    l4=Label(frame,text="Enter Password : ",font=('Montserrat',18,'bold'),bg='#5B8DC0')
    l4.pack()
    l4.place(relx=0.1,rely=0.45)

    l_pass=Entry(frame,width=20,bg="white",relief=GROOVE,borderwidth=5,show="*",font=('Cambria',12,'bold'))
    l_pass.pack(padx=20,pady=40)
    l_pass.place(relx=0.18,rely=0.6)

    def enter_sb(event):
        submit.config(bg="#329E47",width=8,borderwidth=3)
    
    def leave_sb(event):
        submit.config(bg="#0AD432",width=9,borderwidth=2)


    def check_email_validity(event=None):
        # login password and email
        l_email=email.get()
        l_password = l_pass.get()
        # validate email from signup screen
        if not l_email:
            messagebox.showerror(title="Please fill all Information", message="Please enter your email address",parent=w2)
        else:
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(pattern,l_email):
                # check whether account exists in the database
                msg,name=d.confirm_account(l_email,l_password)
                
                def enter_main_screen(event=None):
                    w2.after(1000,w2.destroy())
                    main_screen(name=name)
                if(msg):
                    enter_main_screen()
                elif msg==2:
                    messagebox.showerror(title="Password mismatch", message="Please enter correct password for the email",parent=w2)
                else : 
                    messagebox.showerror(title="Account does not exist", message="Please sign-in to continue",parent=w2)
                    

            else:
                messagebox.showerror(title="Invalid email address", message="Please enter a valid email address",parent=w2)

    #check whether the password is valid from the database if the password is correct prompt user to next window
    submit=Button(frame,text="SUBMIT",width=9,font=('Montserrat',12,"italic"),bg="#0AD432",fg="white",borderwidth=2,relief=RAISED)
    submit.pack()
    submit.place(relx=0.5,rely=0.85,anchor=CENTER)

    submit.bind("<Enter>",enter_sb)
    submit.bind("<Leave>",leave_sb)
    submit.bind("<Button-1>",check_email_validity)

    # submit.bind("<Button-1>",main_screen)

    # footer
    footer = Label(w2, text="© 2024 All rights reserved", font=("Montserrat", 10), bg="#414244", fg="white")
    footer.pack(fill=X,pady=15)
    footer.place(rely=0.97,relx=0.5 ,anchor=CENTER)

    w2.mainloop()

def signup_page(event=None):
    #Sign-Up window here
    #Sign-Up page
    w3=Toplevel()

    w3.title("Theme AI\u2122")
    w3.geometry("650x575+450+100")
    w3.iconbitmap("assets/bot.ico")
    w3.config(bg="#414244")
    # w3.resizable(False,False)

    l=Label(w3,text="Sign-Up",font=("Montserrat",30,"bold"),bg="#414244",fg="white")
    l.pack(padx=10,pady=10)
    l.place(relx=0.5,rely=0.06,anchor=CENTER)

    def enter_login_page(event=None):
        w3.after(500,w3.destroy())
        login_page()

    canvas=Canvas(w3,width=60,height=40,highlightthickness=0,bg='#414244')
    canvas.pack()
    canvas.place(relx=0.01)
    back=canvas.create_text(30,28,text="LOGIN",fill="white",font=("Cambria",12,"underline"))
    canvas.tag_bind(back, "<Button-1>", enter_login_page)

    frame=Frame(w3,relief=GROOVE,bg="#5B8DC0",borderwidth=8,width=500,height=450)
    frame.pack(pady=50)
    frame.place(relx=0.5,rely=0.55,anchor=CENTER)

    l1=Label(frame,text="Enter Email Address*",font=("Montserrat",18,"bold"),bg="#5B8DC0")
    l1.pack(padx=20,pady=20)
    l1.place(relx=0.1,rely=0.05)

    si_email=Entry(frame,width=25,relief=SUNKEN,borderwidth=5,font=("Cambria",12,"bold"))
    si_email.pack(padx=20,pady=8)
    si_email.place(relx=0.15,rely=0.15)

    l2=Label(frame,text="Enter Your Name*",font=("Montserrat",18,"bold"),bg="#5B8DC0")
    l2.pack(padx=20,pady=8)
    l2.place(relx=0.1,rely=0.27)

    name=Entry(frame,width=18,relief=SUNKEN,borderwidth=5,font=("Cambria",12,"bold"))
    name.pack(padx=20,pady=8)
    name.place(relx=0.15,rely=0.37)

    l3=Label(frame,text="New Password*",font=("Montserrat",18,"bold"),bg="#5B8DC0")
    l3.pack(padx=20,pady=20)
    l3.place(relx=0.1,rely=0.49)

    n_pass=Entry(frame,width=10,relief=SUNKEN,borderwidth=5,font=("Cambria",12,"bold"),show="*")
    n_pass.pack(padx=20,pady=8)
    n_pass.place(relx=0.15,rely=0.59)

    l4=Label(frame,text="Confirm Password",font=("Montserrat",18,"bold"),bg="#5B8DC0")
    l4.pack(padx=20,pady=20)
    l4.place(relx=0.1,rely=0.71)

    c_pass=Entry(frame,width=10,relief=SUNKEN,borderwidth=5,font=("Cambria",12,"bold"),show="*")
    c_pass.pack(padx=20,pady=10)
    c_pass.place(relx=0.15,rely=0.81)

    def enter_op(event):
        send_op.config(bg="#46BD74",width=11,borderwidth=4)
    def leave_op(event):
        send_op.config(bg="#46BD74",width=12,borderwidth=4)

    # fetch values from the form
    email=si_email.get()
    sname=name.get()
    pass1=n_pass.get()
    pass2=c_pass.get()

    def check_email_pass_validity(email, sname, pass1, pass2):
        # Regular expressions for email and password validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        password_pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'

        # Validation checks
        if not email:
            messagebox.showerror(title="Warning !!", message="Email field cannot be empty", parent=w3)
        elif not re.match(email_pattern, email):
            messagebox.showerror(title="Invalid email", message="Please enter a valid email address", parent=w3)
        elif not sname:
            messagebox.showerror(title="Name field void", message="Please enter your name", parent=w3)
        elif not pass1 or not pass2:
            messagebox.showerror(title="Password field void", message="Please enter and confirm new password", parent=w3)
        elif pass1 != pass2:
            messagebox.showerror(title="Password Mismatch", message="Passwords do not match", parent=w3)
        elif not re.match(password_pattern, pass1):
            messagebox.showerror(
                title="Enter Valid Password",
                message="Password must contain at least one uppercase letter, one lowercase letter, one numeric digit, and be 8 or more characters long",
                parent=w3
            )
        else:
            # All validations passed, proceed to the next step
            return True
        return False
    
    def entering_otp_validation(event=None):
        # Fetch values from the form fields inside the function
        email = si_email.get()
        sname = name.get()
        pass1 = n_pass.get()
        pass2 = c_pass.get()

        valid = check_email_pass_validity(email, sname, pass1, pass2)
        if valid:
            # otp validation screen
            w3.after(500,w3.destroy())
            ov.enter_otp_screen(email, sname, pass2)
            
    # send_otp button 
    send_op=Button(frame,text="Send OTP",bg="#46BD74",fg="white",width=12,relief=FLAT,borderwidth=2,font=("Montserrat",12,"bold"))
    send_op.pack()
    send_op.place(relx=0.5,rely=0.95,anchor=CENTER)
    
    send_op.bind("<Enter>",enter_op)
    send_op.bind("<Leave>",leave_op)
    send_op.bind("<Button-1>",entering_otp_validation)

    # footer
    footer = Label(w3, text="© 2024 All rights reserved", font=("Montserrat", 10), bg="#414244", fg="white")
    footer.pack(side=BOTTOM,fill=X,pady=15)

    # mainloop
    w3.mainloop()

def main_screen(name=None,event=None):
    # main window
    #chat page
    w4=Toplevel()
    
    w4.title("Theme AI\u2122")
    w4.geometry("650x575+500+100")
    w4.iconbitmap("assets/bot.ico")
    w4.config(bg="#414244")

    greet=StringVar()
    greet.set(f"Welcome {name}!!")

    l=Label(w4,textvariable=greet,font=("Consolas",20,"bold"),bg="#414244",fg="white")
    l.pack()
    l.place(relx=0.5,rely=0.3,anchor=CENTER)

    intro='''Welcome to the Theme AI\u2122! 
    Select a category for specific queries and innovate with your skills.

    Press 'enter' to continue....
            '''
    l1=Label(w4,text=intro,font=("Montserrat",14,'italic'),bg="#414244",fg="white")
    l1.pack()
    l1.place(relx=0.5,rely=0.5,anchor=CENTER)

    def entering_chat_screen(event=None):
        w4.after(500,w4.destroy())
        m.chat_screen()
        
    w4.bind("<KeyPress>",entering_chat_screen)

    # footer
    footer = Label(w4, text="© 2024 All rights reserved", font=("Montserrat", 10), bg="#414244", fg="white")
    footer.pack(side=BOTTOM,fill=X,pady=15)

    w4.mainloop()

#MAIN FUNCTIONS :-
if __name__ == "__main__":
    landing_page()