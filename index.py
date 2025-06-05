from customtkinter import *
from PIL import Image
import tkinter as tk  
from tkinter import ttk
from tkinter import messagebox
import database
root = CTk() 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 950
window_height = 570
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(0, 0)
root.title('Latry Management System')

image = CTkImage(Image.open('img/add.jpg'), size=(950, 200))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.grid(row=0,column=0,columnspan=2)
# Function to open a new window
import importlib 
import sys  

def open_new_window():
    if "up_latry" in sys.modules:
        del sys.modules["up_latry"]  
    import up_latry
    importlib.reload(up_latry)

def open_new_window2():
    if "jama_latry" in sys.modules:
        del sys.modules["jama_latry"]  
    import jama_latry
    importlib.reload(jama_latry)
def open_new_window3():
    if "JamaUp_latry" in sys.modules:
        del sys.modules["JamaUp_latry"]  
    import JamaUp_latry
    importlib.reload(JamaUp_latry)
 
def new_member():
   clear()
   tree.selection_remove(tree.focus)
   
def search_member():
   if searchEntry.get()=='':
      messagebox.showerror('Error','search field are required')        
   elif searchcombobox.get()=='Search By':
          messagebox.showerror('Error','please select an option') 
   else:
      searched_member=database.search(searchcombobox.get(),searchEntry.get())
      
      tree.delete(*tree.get_children())
      for member in searched_member:
          tree.insert('',END,values=member)   
          
def showall_member():
   treeview_data()   
   searchEntry.delete(0,END)        
   searchcombobox.set('Search By') 
     
def clear():
    userIdEntry.delete(0,END)
    usernameEntry.delete(0,END)
    emailEntry.delete(0,END)
    phoneEntry.delete(0,END)
    Adhar_noEntry.delete(0,END)
    AddressEntry.delete(0,END)
    
def selection(evet):
   selected_item=tree.selection()
   if selected_item:
      row=tree.item(selected_item)['values']
      clear()
      userIdEntry.insert(0,row[0])
      usernameEntry.insert(0,row[1])
      emailEntry.insert(0,row[2])
      phoneEntry.insert(0,row[3])
      Adhar_noEntry.insert(0,row[4])
      AddressEntry.insert(0,row[5])
   
def treeview_data():
   members=database.fatch_member()
   tree.delete(*tree.get_children())
   for member in members:
      tree.insert('',END,values=member)
      
def new_member():
   clear()
   tree.selection_remove(tree.focus())
            
def add_member():
   if userIdEntry.get()==''or usernameEntry.get()==''or emailEntry.get()=='' or phoneEntry.get()==''or Adhar_noEntry.get()==''or AddressEntry.get()=='':
      messagebox.showerror("error","all field are required")
   elif database.id_exists(userIdEntry.get()):
      messagebox.showerror('error','Id alordy is exists')
   else: 
      database.insert(userIdEntry.get(),usernameEntry.get(),emailEntry.get(),phoneEntry.get(),Adhar_noEntry.get(),AddressEntry.get())
      treeview_data()
      clear()  
    
def update_member(): 
   selected_item=tree.selection()
   if not selected_item:
      messagebox.showerror('Error','select dat to update')
   else:
      database.update(userIdEntry.get(),usernameEntry.get(),emailEntry.get(),phoneEntry.get(),Adhar_noEntry.get(),AddressEntry.get())
      treeview_data()
      clear()
      messagebox.showinfo('successfully','member detail update')
   
def delete_member():
   selected_item=tree.selection()
   if not selected_item:
      messagebox.showerror('Error','select member are deleted')
   else:
      database.delete(userIdEntry.get())
      treeview_data()
      clear()
      messagebox.showerror('successfully','select member to deleted')
      
def deleteall_member(): 
   result=messagebox.askyesno('Confire','Do you really want to delete all the member ')
   if result:
      database.deleteall()
   
# Use tk.Menu instead of just Menu
menubar = tk.Menu(root)  
addmember = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Register Member', menu=addmember)
Up_latry = tk.Menu(menubar, tearoff=0)
Up_latry.add_command(label="Open Window", command=open_new_window)  
menubar.add_cascade(label='draw Latry', menu=Up_latry)
Jama_latry = tk.Menu(menubar, tearoff=0)
Jama_latry.add_command(label="Open Window", command=open_new_window2)  
menubar.add_cascade(label=' submit monthly Latry', menu=Jama_latry)
JamaUp_latry = tk.Menu(menubar, tearoff=0)
JamaUp_latry.add_command(label="Open Window", command=open_new_window3)  
menubar.add_cascade(label='submit draw Latry', menu=JamaUp_latry)
root.configure(menu=menubar)
 
liftFrame=CTkFrame(root,height=300,width=400,fg_color='blue')
liftFrame.grid(row=1,column=0)
userIdlable=CTkLabel(liftFrame,text='UserId',font=('Goudy Old Style ',15,'bold'))
userIdlable.grid(row=0,column=0,padx=20,pady=10,sticky='w')
userIdEntry=CTkEntry(liftFrame,placeholder_text='Enter user Id',width=250)
userIdEntry.grid(row=0,column=1)
usernamelable=CTkLabel(liftFrame,text='Username',font=('Goudy Old Style ',15,'bold'))
usernamelable.grid(row=1,column=0,padx=20,pady=10,sticky='w')
usernameEntry=CTkEntry(liftFrame,placeholder_text='Enter user name',width=250)
usernameEntry.grid(row=1,column=1)
emaillable=CTkLabel(liftFrame,text='E-mail',font=('Goudy Old Style ',15,'bold'))
emaillable.grid(row=2,column=0,padx=20,pady=10,sticky='w')
emailEntry=CTkEntry(liftFrame,placeholder_text='Enter user email',width=250)
emailEntry.grid(row=2,column=1)
phonelable=CTkLabel(liftFrame,text='Phone_no',font=('Goudy Old Style ',15,'bold'))
phonelable.grid(row=3,column=0,padx=20,pady=10,sticky='w')
phoneEntry=CTkEntry(liftFrame,placeholder_text='Enter user phone',width=250)
phoneEntry.grid(row=3,column=1)
Adhar_nolable=CTkLabel(liftFrame,text='Adhar_no',font=('Goudy Old Style ',15,'bold'))
Adhar_nolable.grid(row=4,column=0,padx=20,pady=10,sticky='w')
Adhar_noEntry=CTkEntry(liftFrame,placeholder_text='Enter user Adhar_no',width=250)
Adhar_noEntry.grid(row=4,column=1)
Addresslable=CTkLabel(liftFrame,text='Address',font=('Goudy Old Style ',15,'bold'))
Addresslable.grid(row=5,column=0,padx=20,pady=10,sticky='w')
AddressEntry=CTkEntry(liftFrame,placeholder_text='Enter user Address',width=250)
AddressEntry.grid(row=5,column=1)
# Right Frame (Increase width)
rightFrame = CTkFrame(root, height=300, width=650)  # Increased width
rightFrame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
# Search Box and Buttons
search_options = ['userId', 'Username', 'E-mail', 'Phone_no', 'Adhar_no', 'Address']
searchcombobox = CTkComboBox(rightFrame, values=search_options, state='readonly')
searchcombobox.set('Search By')
searchcombobox.grid(row=0, column=0, padx=5, pady=5)
searchEntry = CTkEntry(rightFrame, placeholder_text='', width=150)
searchEntry.grid(row=0, column=1, padx=5, pady=5)
searchbutton = CTkButton(rightFrame, text='Search', width=100,command=search_member)
searchbutton.grid(row=0, column=2, padx=5, pady=5)
showallbutton = CTkButton(rightFrame, text='showAll', width=100,command=showall_member)
showallbutton.grid(row=0, column=3, padx=5, pady=5)

# Create Treeview
tree = ttk.Treeview(rightFrame, columns=('Id', 'Username', 'E-mail', 'Phone_no', 'Adhar_no', 'Address'), 
                    show='headings', height=10)
tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL,command=tree.yview )
scrollbar.grid(row=1, column=4,sticky='ns')

scrollbar = ttk.Scrollbar(rightFrame, orient=HORIZONTAL, command=tree.xview)
scrollbar.grid(row=2, column=0, columnspan=4, sticky="ew")

# Define column headings
tree.heading('Id', text='User ID')
tree.heading('Username', text='Username')
tree.heading('E-mail', text='E-mail')
tree.heading('Phone_no', text='Phone No')
tree.heading('Adhar_no', text='Aadhar No')
tree.heading('Address', text='Address')

# Set column widths (adjusted)
tree.column('Id', width=50, anchor='center')
tree.column('Username', width=100, anchor='w')
tree.column('E-mail', width=100, anchor='w')
tree.column('Phone_no', width=100, anchor='center')
tree.column('Adhar_no', width=100, anchor='center')
tree.column('Address', width=100, anchor='w')
treeview_data()
#create button frame
buttonframe=CTkFrame(root)
buttonframe.grid(row=2,column=0,columnspan=2)
newmemberbutton = CTkButton(buttonframe, text='New member',  width=150,command=new_member)
newmemberbutton.grid(row=0, column=0, padx=5, pady=5)
Addmemberbutton = CTkButton(buttonframe, text='Add member',  width=150,command=add_member)
Addmemberbutton.grid(row=0, column=1, padx=5, pady=5)
Updatememberbutton = CTkButton(buttonframe, text='Update member',  width=150,command=update_member)
Updatememberbutton.grid(row=0, column=2, padx=5, pady=5)
deletemberbutton = CTkButton(buttonframe, text='delete member', width=150,command=delete_member)
deletemberbutton.grid(row=0, column=3, padx=5, pady=5)
deleteallmberbutton = CTkButton(buttonframe, text='delete all member',  width=150,command=deleteall_member)
deleteallmberbutton.grid(row=0, column=4, padx=5, pady=5)
root.bind('<ButtonRelease>',selection)
root.mainloop()
