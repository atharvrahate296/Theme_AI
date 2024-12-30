from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import google.generativeai as genai
from dotenv import load_dotenv
import sys
import os

def chat_screen(event=None):
    # chat window
    w5 = Tk()

    w5.title("Theme AI\u2122")
    w5.geometry("1100x680+180+80")
    w5.iconbitmap("assets/bot.ico")
    w5.config(bg="#414244")
    w5.attributes('-fullscreen', True)

    def toggle_fullscreen(event):
        w5.attributes('-fullscreen', True)

    def exit_fullscreen(event):
        w5.attributes('-fullscreen', False)

    w5.bind("<Control-f>", toggle_fullscreen)
    w5.bind("<Escape>", exit_fullscreen)

    l = Label(w5, text="Theme AI", font=("Georgia", 34, "bold"), bg="#414244", fg="white")
    l.pack(pady=20)

    categories = [
    'Programming & Development',
    'Culinary & Recipes',
    'Writing & Creativity',
    'Language & Communication',
    'Health & Fitness',
    'Travel & Tourism',
    'Personal Finance & Investing'
]

    # outer frame
    frame = Frame(w5, width=1200, height=760, borderwidth=3, relief=GROOVE, bg="#414244")
    frame.pack(pady=20)

    l1 = Label(frame, text="Select a Theme", font=("Montserrat", 15, "bold"), bg="#414244", fg="white")
    l1.place(relx=0.02, rely=0.05)

    category = ttk.Combobox(frame, values=categories, width=25, font=("Times New Roman", 12, 'bold'))
    category.set('general')
    category.place(relx=0.03, rely=0.1)

    chat_history_frame = Frame(frame, bg="#2c2c2c", relief=GROOVE, borderwidth=4)  # Added border for contrast
    chat_history_frame.place(relx=0.5, rely=0.15, anchor=N, width=1100, height=450)

    chat_history = Text(chat_history_frame, borderwidth=3, width=70, height=3, relief=SUNKEN, font=("Georgia", 14), bg="#2c2c2c", fg="white", padx=10, pady=10)
    chat_history.pack(side=LEFT, fill=BOTH, expand=True)
    chat_history.config(state=DISABLED)

    scrollbar = Scrollbar(chat_history_frame, orient=VERTICAL, command=chat_history.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    chat_history.config(yscrollcommand=scrollbar.set)


    prompt = Text(frame, width=88, height=4, relief=SUNKEN, borderwidth=3, font=("Georgia", 14), bg="#2c2c2c", fg="white", padx=10, pady=10)
    prompt.place(relx=0.5, rely=0.86, anchor=CENTER)
    prompt.insert(1.0, "Enter a prompt")

    def enter_prompt(event=None):
        prompt.config(highlightbackground="green", highlightthickness=2)

    def exit_prompt(event=None):
        prompt.config(highlightbackground="#414244", highlightthickness=0)

    prompt.bind("<Enter>", enter_prompt)
    prompt.bind("<Leave>", exit_prompt)
    chat_history.insert(1.0, "Ask me anything.....")

    def query_n_response(event=None):
        role = category.get()

        query = prompt.get('1.0', 'end').strip()
        if query.lower() in ["end", "exit", "stop"]:
            exit_app()
            return
        elif query.lower() in ["clear"]:
            chat_history.config(state=NORMAL)
            chat_history.delete('1.0', END)  # Clear the chat history
            chat_history.config(state=DISABLED)
            prompt.delete('1.0', END)  # Clear the prompt input
            return
        

        load_dotenv()  # Load the environment variables from the .env file

        api = os.getenv("API_KEY")  # Access the API key securely

        # api = API_KEY  # Replace with your actual API key
        genai.configure(api_key=api)
        
        # Store and consider chat history
        chat_history_content = chat_history.get("1.0", "end-1c")  # Get existing chat history

        # Update the system prompt to include chat history
        system_instruction = f"You are a {role} chatbot. Answer questions related to {role} and nothing outside of it. Here is the conversation history:\n{chat_history_content}\n"

        # Create the model with the updated system prompt
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )

        # Generate the response using the query
        response = model.generate_content(query)

        # Insert the query and response into the chat history
        chat_history.config(state=NORMAL, font=("Georgia", 14))
        chat_history.insert(END, "You : " + query + "\n")
        chat_history.insert(END, "\n")  # Adds padding after the message
        chat_history.insert(END, "Theme_AI : " + response.text + "\n\n")
        chat_history.config(state=DISABLED)
        chat_history.yview(END)

        # Clear the input prompt
        prompt.delete('1.0', END)

    prompt.bind("<Return>", query_n_response)

    enter_button = Button(frame, width=5, text="Send", font=('Georgia', 14, 'bold'), fg="white", bg="green", relief=RAISED, borderwidth=3, command=query_n_response)
    enter_button.place(relx=0.94, rely=0.895, anchor=E)
    enter_button.config(highlightbackground="#2c2c2c", highlightcolor="green", highlightthickness=0)

    def enter_button_hover(event=None):
        enter_button.config(bg="dark green",highlightthickness=1)

    def exit_button_hover(event=None):
        enter_button.config(bg="green",highlightthickness=0)

    enter_button.bind("<Enter>", enter_button_hover)
    enter_button.bind("<Leave>", exit_button_hover)

    # Exit button functionality
    def exit_app(event=None):
        w5.after(500,w5.destroy())
        exit_screen()

    exit_button = Button(w5, width=4, text="X", font=('Georgia', 12, 'bold'), fg="black", bg="gray", command=exit_app)
    exit_button.place(relx=0.998, rely=0.02, anchor=E)

    # Adjust label positions slightly higher to ensure visibility
    lf = Label(frame, text="Press Ctrl+f to enter fullscreen", font=('Consolas', 10), bg="#414244", fg="white")
    lf.place(relx=0.04, rely=0.955)  # Adjusted position


    lg = Label(frame, text="end=exit, stop=exit, clear=clear chat", font=('Consolas', 10), bg="#414244", fg="white")
    lg.place(relx=0.5, rely=0.97,anchor=CENTER)  # Adjusted position

    ef = Label(frame, text="Press esc to exit fullscreen", font=('Consolas', 10),bg="#414244", fg="white")
    ef.place(relx=0.82, rely=0.955)  # Adjusted position
    
    # Add footer label to the bottom of the window
    footer = Label(w5, text="\u00a9 2024 All rights reserved", font=("Georgia", 12), bg="#414244", fg="white", pady=5)
    footer.place(relx=0.5,rely=0.985,anchor=CENTER) 

    w5.mainloop()
def exit_screen(event=None):
    root= Toplevel()

    root.title("Theme AI\u2122")
    root.geometry("1100x680+180+80")
    root.iconbitmap("assets/bot.ico")
    root.config(bg="#414244")
    root.attributes('-fullscreen', True)

    msg = '''
                    Thank you for using Theme AI.
    Please Keep learning and explore more use cases for the app.

    Thank you,

    Team, Theme AI
    :)
    '''
    greet = StringVar()
    greet.set(msg)
    def exit(event=None):
        root.destroy()
        sys.exit()
    message = Label(root,textvariable = greet , font =("Montserrat",20,'bold'),fg="white",bg="#414244")
    message.place(relx=0.5,rely=0.5,anchor=CENTER)

    footer = Label(root, text="\u00a9 2024 All rights reserved", font=("Georgia", 12), bg="#414244", fg="white", pady=5)
    footer.pack(side=BOTTOM)
    root.bind("<KeyPress>",exit)

    root.mainloop()


# if __name__ == '__main__':
#     chat_screen()
