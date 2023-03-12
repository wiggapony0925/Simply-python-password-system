import os     
from tkinter import *


def log_user():
    global login_password, login_username
    login_password = log_password.get()
    login_username = log_username.get()
    
    log_username_entry.delete(0, END)
    log_password_entry.delete(0, END)
        
    list_of_files = os.listdir()
    if log_username == list_of_files:       #check if its log_user or login_user
        for files in list_of_files:
            if log_username == "private_information":
                continue
        file1 = open(username_info, "r")  ##VARIABLE FIX 
        verify = file1.read().splitlines() 
        if log_password in verify: 
           print("log in success")
        else:
            print("Failed Log in")
    else:
        print("user isn't in the database")
    
    #if True: 
   #     Label(screen1, text = "Login complete" ,fg ="green", font = ("calabri", 11)).pack()
        
        
def register_user(): 
    global username_info, password_info
    username_info = username.get()
    password_info = password.get()
    
    file = open("private_information", "a")   
    file.write(f"USERNAME:{username_info}\n")    
    file.write(f"PASSWORD: {password_info}\n")
    file.write("________________\n")
    file.close()
    
    register_file = open(username_info, "w")
    register_file.write(username_info+"\n")
    register_file.write(password_info)
    register_file.close()
                
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text = "Registration complete" ,fg ="green", font = ("calabri", 11)).pack()
         
def register():
    global screen1,username_entry,password_entry
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username, password
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text = "please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username : ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password : ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Button(screen1,text = "Register", width = 10, height = 1, command=register_user).pack()


def login():
    global screen2,log_password ,log_username,log_username_entry ,log_password_entry
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    log_password = StringVar()
    log_username = StringVar()
    
    Label(screen2, text = "please enter details below").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Username: ").pack() #command
    log_username_entry = Entry(screen2, textvariable= log_username)
    log_username_entry.pack()
    Label(screen2, text = "Password: ").pack()
    log_password_entry = Entry(screen2, textvariable= log_password)
    log_password_entry.pack()
    Button(screen2, text = "Log in", width = 10, height = 1, command = log_user).pack()
    

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey",width = "300", height = "2",font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = '2', width = "30",command=login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = '2', width = "30", command=register).pack()   
    
    screen.mainloop()

main_screen()
register()
register_user()
login()
log_user()
