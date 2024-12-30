# import necessary libraries for tkinter GUI and OTP generation
import random as r
from tkinter import *
from tkinter import messagebox
import data as d

# import necessary libraries to send Email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

otp = ""
sender = "themeaiorg@gmail.com"  
password = "bkwt vzas pbmj qent"  

def generate_otp(recipient):
    global otp
    otp = ''
    length = 6
    for i in range(length):
        otp += str(r.randint(0, 9))
    return send_otp_to_mail(sender, password, recipient, otp)

def send_otp_to_mail(sender, password, recipient, otp):
    def create_message(sender, recipient, subject, otp):
        message = MIMEMultipart('alternative')
        message['to'] = recipient
        message['from'] = sender
        message['subject'] = subject
        
        html_message_text = f"""
        <html>
        <body>
            <p>Dear User,</p>
            <p>To authenticate your account with <strong>THEME AI</strong>, please use the following code to verify your email account:</p>
            <p><strong style="font-size: 20px;">{otp}</strong></p>
            <p>If you did not request this code, please ignore this email.</p>
            <p>Thank you,<br>Theme_AI Team</p>
        </body>
        </html>
        """
        part = MIMEText(html_message_text, 'html')
        message.attach(part)
        
        return message

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        logging.info("Logged in to SMTP server successfully")

        subject = 'Verify Your OTP for Sign-Up'
        message = create_message(sender, recipient, subject, otp)
        
        server.sendmail(sender, recipient, message.as_string())
        logging.info(f"Message sent to {recipient}")
        server.quit()
        
        return True
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False

def enter_otp_screen(s_email, sname, pass2):
    if generate_otp(s_email):
        # OTP validation page
        w5 = Toplevel()
        w5.title("Theme AI\u2122")
        w5.geometry("650x600+450+100")
        w5.iconbitmap("assets/bot.ico")
        w5.config(bg="#414244")

        email_sent_label = Label(w5, text="Email has been sent !!", font=('Montserrat', 18, 'bold'), bg="#414244", fg="green")
        email_sent_label.pack()
        email_sent_label.place(relx=0.5, rely=0.08, anchor=CENTER)

        message = '''Please check your email for a 6-digit confirmation OTP 
                to confirm your signup process...'''

        t1 = Label(w5, text=message, font=('Montserrat', 18, 'bold'), bg="#414244", fg="white")
        t1.pack()
        t1.place(relx=0.5, rely=0.4, anchor=CENTER)

        label=Label(w5, text="Enter OTP : ", font=('Montserrat',16), bg="#414244", fg="white")
        label.pack()
        label.place(relx=0.3, rely=0.55, anchor=CENTER)

        otp_c = Entry(w5, width=7, font=('Cambria', 15, 'bold'), relief=SUNKEN, borderwidth=5)
        otp_c.pack()
        otp_c.place(relx=0.5, rely=0.55, anchor=CENTER)

        def enter_op(event):
            check.config(bg="#46BD74", width=11, borderwidth=4)

        def leave_op(event):
            check.config(bg="#5471e3", width=12, borderwidth=4)

        def confirm_otp(event=None):
            if otp_c.get() == otp:
                s = Label(w5, text='OTP validated successfully !!', font=('Montserrat', 22, 'bold'), bg='#414244', fg='white')
                s.pack(padx=20, pady=10)
                s.place(relx=0.5, rely=0.8, anchor=CENTER)

                # Call function to write the user data to database
                w5.after(5000, w5.destroy)
                d.write_data(sname, s_email, pass2)
                
            else:
                messagebox.showerror(title="Error", message="Incorrect OTP", parent=w5)

        check = Button(w5, text="CONFIRM", bg="#5471e3", fg="white", width=12, relief=FLAT, borderwidth=2, font=("Montserrat", 12, "bold"))
        check.pack()
        check.place(relx=0.5, rely=0.7, anchor=CENTER)

        check.bind("<Button-1>", confirm_otp)
        check.bind("<Enter>", enter_op)
        check.bind("<Leave>", leave_op)

        resend = Label(w5, text="resend OTP", font=('Cambria', 12, 'underline'), bg="#414244", fg='white')
        resend.pack()
        resend.place(relx=0.5, rely=0.6, anchor=CENTER)

        resend.bind("<Button-1>", lambda event: generate_otp(s_email))

        w5.mainloop()
    else:
        messagebox.showerror(title="Error", message="Failed to send OTP email")

# enter_otp_screen(recipient)
