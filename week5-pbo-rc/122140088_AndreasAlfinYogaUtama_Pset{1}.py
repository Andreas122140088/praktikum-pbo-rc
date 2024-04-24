import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Login:
  def __init__(self,root):
    self.root = root
        
    self.window=root
    self.window.title("Login")
    self.window.minsize(400,200)
  
    self.frame = ttk.Frame(self.window)
    self.frame.pack(pady=10, padx=10)
    #username label
    self.username_label = ttk.Label(self.frame, text="Username:")
    self.username_label.pack(pady=5)
    
    #username entry
    self.username_entry = ttk.Entry(self.frame)
    self.username_entry.pack(pady=5)
    
    #password label
    self.password_label = ttk.Label(self.frame, text="Password:")
    self.password_label.pack(pady=5)
    
    #password entry
    self.password_entry = ttk.Entry(self.frame, show="*")
    self.password_entry.pack(pady=5)
    
    #data user
    self.data_user = {}
    
    #button login
    self.button = ttk.Button(self.frame, text="Login",
    command=lambda: show_message()
    if self.username_entry.get() in self.data_user
    and self.password_entry.get() in self.data_user[self.username_entry.get()] 
    else wrong_password())
    self.button.pack(pady=10)

    #button Regis
    self.button = ttk.Button(self.frame, text="Register",
    command=lambda:sign_up(self))
    
    def sign_up(self):
      self.window.withdraw()
      self.win_reg = Register_form(self.window,self.data_user)
      # self.win_reg.
    self.button.pack(pady=10)
    def show_message():
      messagebox.showinfo("Login succesful!",f"Welcome to the program ! \n{self.username_entry.get()}")
    def wrong_password():
      messagebox.showwarning("Error", "Incorrect username or password. Please try again.")

class Register_form:
  def __init__(self,master,user):
    self.master = master
    self.user = user

    self.window_reg=tk.Toplevel(self.master)
    self.window_reg.title("Login")
    self.window_reg.minsize(400,200)

    self.frame = ttk.Frame(self.window_reg)
    self.frame.pack(pady=10, padx=10)
    #username label
    self.username_label = ttk.Label(self.frame, text="Username:")
    self.username_label.pack(pady=5)

    #username entry
    self.username_entry = ttk.Entry(self.frame)
    self.username_entry.pack(pady=5)

    #password label
    self.password_label = ttk.Label(self.frame, text="Password:")
    self.password_label.pack(pady=5)

    #password entry
    self.password_entry = ttk.Entry(self.frame, show="*")
    self.password_entry.pack(pady=5)

    #data user
    self.data_user = {}

    # register
    self.button = ttk.Button(self.frame, text="Register",
    command=lambda: do_register(self))
    self.button.pack(pady=10)

    def do_register(self):
      username = self.username_entry.get()
      password = self.password_entry.get()

      if not username or not password:
        messagebox.showwarning("Error", "Please enter username and password.")
        return
      if username in self.data_user:
        messagebox.showwarning("Error", "Username already exists. Please choose a different username.")
        return

      self.user[username] = password
      messagebox.showinfo("Success", "Registration successful.")
      self.window_reg.destroy()
      self.master.deiconify()

root = tk.Tk()
home = Login(root)
root.mainloop()
