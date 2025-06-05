from customtkinter import *
from PIL import Image 
from tkinter import messagebox
import customtkinter
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','all fild is required')
    elif usernameEntry.get()=='shiv' or passwordEntry.get()=='4321':
        messagebox.showinfo("success",'successfully login')
        root.destroy()
        import index
    else:
        messagebox.showerror('Error','worng credetials')
   
root = CTk()  
root.title("latry management")
root.geometry("950x500")  
root.resizable(0,0)
image=CTkImage(Image.open ('img/login.jpg'),size=(950,500))
imageLable=CTkLabel(root,image=image,text='')
imageLable.place(x=0,y=0)
headlable=CTkLabel(root,text="Latry managemant system",bg_color='#fafafa',font=('Goudy Old Style ',20,'bold'))
headlable.place(x=650,y=100)
usernameEntry=CTkEntry(root,placeholder_text='Enter user name',width=230)
usernameEntry.place(x=660,y=150)
passwordEntry=CTkEntry(root,
placeholder_text='Enter user password',width=230,show='*')
passwordEntry.place(x=660,y=200)
loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=700,y=250)
root.mainloop()

