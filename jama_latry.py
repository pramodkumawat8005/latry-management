from customtkinter import *
from PIL import Image
import tkinter as tk  
from tkinter import ttk
from tkinter import messagebox
import database
root = CTk() 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1000
window_height = screen_height
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(0, 0)
root.title('Latry Management System')

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
    phoneEntry.delete(0,END)
    latryamountEntry.delete(0,END)
   
def selection(evet):
   selected_item=tree.selection()
   if selected_item:
      row=tree.item(selected_item)['values']
      clear()
      userIdEntry.insert(0,row[0])
      usernameEntry.insert(0,row[1])
      phoneEntry.insert(0,row[3])
      
def treeview_data():
   members=database.fatch_member()
   tree.delete(*tree.get_children())
   for member in members:
      tree.insert('',END,values=member)
      
def treeview_data1():
   members=database.fatch_jamalatry()
   tree1.delete(*tree1.get_children())
   for member in members:
      tree1.insert('',END,values=member)   
         
def new_member():
   clear()
   tree.selection_remove(tree.focus())
  
         
        
def jamalatry():
   if userIdEntry.get()==''or usernameEntry.get()==''or phoneEntry.get()==''or latryamountEntry.get()=='':
      messagebox.showerror("error","all field are required")
   elif database.id_exists1(userIdEntry.get()):
      messagebox.showerror('error','Id alordy is exists')
   else: 
     Total=database.findTotal(userIdEntry.get(),latryamountEntry.get(),late_chargeEntry.get())
     if Total==None:
        Total=latryamountEntry.get()
     database.insert1(userIdEntry.get(),usernameEntry.get(),phoneEntry.get(),latryamountEntry.get(),late_chargeEntry.get(),Total)
     treeview_data1()
     clear()
    
def Storedata():
    result=messagebox.askyesno('Confire','Have you collected all latry members latry then click "Yes" otherwise click "No ')
    if result:
         database.copyjamalatry()
         database.deleteall1()    
         treeview_data1()
 
liftFrame=CTkFrame(root,height=300,width=400,fg_color='blue')
liftFrame.grid(row=1,column=0)
userIdlable=CTkLabel(liftFrame,text='UserId',font=('Goudy Old Style ',15,'bold'))
userIdlable.grid(row=0,column=0,padx=20,pady=10,sticky='w')
userIdEntry=CTkEntry(liftFrame,placeholder_text='Enter user Id',width=240)
userIdEntry.grid(row=0,column=1)
usernamelable=CTkLabel(liftFrame,text='Username',font=('Goudy Old Style ',15,'bold'))
usernamelable.grid(row=1,column=0,padx=20,pady=10,sticky='w')
usernameEntry=CTkEntry(liftFrame,placeholder_text='Enter user name',width=240)
usernameEntry.grid(row=1,column=1)
phonelable=CTkLabel(liftFrame,text='Phone_no',font=('Goudy Old Style ',15,'bold'))
phonelable.grid(row=2,column=0,padx=20,pady=10,sticky='w')
phoneEntry=CTkEntry(liftFrame,placeholder_text='Enter user phone',width=240)
phoneEntry.grid(row=2,column=1)
latryamountlable=CTkLabel(liftFrame,text='Amount',font=('Goudy Old Style ',15,'bold'))
latryamountlable.grid(row=3,column=0,padx=20,pady=10,sticky='w')
latryamountEntry=CTkEntry(liftFrame,placeholder_text='Enter latryAmount',width=240)
latryamountEntry.grid(row=3,column=1)

late_chargelable=CTkLabel(liftFrame,text='Late_charge',font=('Goudy Old Style ',15,'bold'))
late_chargelable.grid(row=4,column=0,padx=20,pady=10,sticky='w')
late_charge_var = tk.StringVar(value="0")  # Default value set to 50

# Create the Entry with the variable
late_chargeEntry =CTkEntry(liftFrame, textvariable=late_charge_var, width=240)
late_chargeEntry.grid(row=4, column=1)
# Totallable=CTkLabel(liftFrame,text='Total',font=('Goudy Old Style ',15,'bold'))
# Totallable.grid(row=5,column=0,padx=20,pady=10,sticky='w')
# TotalEntry=CTkEntry(liftFrame,placeholder_text='Enter Total',width=240)
# TotalEntry.grid(row=5,column=1)
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
tree.bind('<<TreeviewSelect>>', selection)



buttonframe=CTkFrame(root)
buttonframe.grid(row=2,column=0,columnspan=2)
newmemberbutton = CTkButton(buttonframe, text='New member',  width=150,command=new_member)
newmemberbutton.grid(row=0, column=0, padx=5, pady=5)
jamalatrybutton = CTkButton(buttonframe, text='jamalatry',  width=150,command=jamalatry)
jamalatrybutton.grid(row=0, column=1, padx=5, pady=5)
Storedatabutton = CTkButton(buttonframe, text='Storedata',  width=150,command=Storedata)
Storedatabutton.grid(row=0, column=2, padx=5, pady=5)
jamaentryFrame = CTkFrame(root, height=170, width=800)
jamaentryFrame.grid(row=3, column=0, columnspan=2, padx=10, pady=10,)
#new treeview for show jamalatry
tree1 = ttk.Treeview(jamaentryFrame, columns=('Id', 'Username',  'Phone_no', 'Amount','late_charge','Total','Date'), 
                    show='headings', height=10)
tree1.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

scrollbar = ttk.Scrollbar(jamaentryFrame, orient=VERTICAL,command=tree.yview )
scrollbar.grid(row=1, column=4,sticky='ns')

scrollbar = ttk.Scrollbar(jamaentryFrame, orient=HORIZONTAL, command=tree.xview)
scrollbar.grid(row=2, column=0, columnspan=4, sticky="ew")

# Define column headings
tree1.heading('Id', text='User ID')
tree1.heading('Username', text='Username')
tree1.heading('Phone_no', text='Phone No')
tree1.heading('Amount', text='Amount')
tree1.heading('late_charge', text='late_charge')
tree1.heading('Total', text='Total')
tree1.heading('Date', text='Date')
# Set column widths (adjusted)
tree1.column('Id', width=50, anchor='center')
tree1.column('Username', width=100, anchor='center')
tree1.column('Phone_no', width=100, anchor='center')
tree1.column('Amount', width=100, anchor='center')
tree1.column('late_charge', width=150, anchor='center')
tree1.column('Total', width=100, anchor='center')
tree1.column('Date', width=150, anchor='center')

treeview_data1()


tree.bind('<<TreeviewSelect>>', selection)

root.mainloop()
