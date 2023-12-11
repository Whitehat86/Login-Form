import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title('Login Form')
window.geometry('340x200')
window.configure(bg='#ECE2DF')

def login():
  username = 'aaaa'
  password = '111111'
  if username_entry.get()== username and password_entry.get()== password:
    messagebox.showinfo(title='Login Succesful', message='You have logged in successfully')
  else:
    messagebox.showerror(title='Unsuccessful Login', message='Username or Password is incorrect')
    
  
frame = tkinter.Frame(window, bg= '#ECE2DF')

#create widgets on the screen
login_label = tkinter.Label(frame, text='Login', font = ('Arial', 18), bg='#ECE2DF')
username_label = tkinter.Label(frame, text='Username',font=('Arial', 14), bg='#ECE2DF') 
username_entry =tkinter.Entry(frame,font=('Arial', 10))
password_label = tkinter.Label(frame, text='Password',font=('Arial', 14), bg='#ECE2DF')
password_entry = tkinter.Entry(frame, show='*', font=('Arial', 10))
login_button=tkinter.Button(frame, text ='Login',font=('Arial', 14), bg='#ECE2DF', command = login)

#placing widgets on the screen
login_label.grid(row = 0, column = 0, columnspan=2, sticky='news',pady=10)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1,pady=5)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1,pady=5)
login_button.grid(row=3, column=0,columnspan=2,pady=8)

frame.pack()

window.mainloop()