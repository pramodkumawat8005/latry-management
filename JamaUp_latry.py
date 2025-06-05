from customtkinter import *
from PIL import Image
import tkinter as tk  
from tkinter import ttk
from tkinter import messagebox
import database
import math  # Add this at the top of your file

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
   tree3.selection_remove(tree3.focus)
def search_member():
   if searchEntry.get()=='':
      messagebox.showerror('Error','search field are required')        
   elif searchcombobox.get()=='Search By':
          messagebox.showerror('Error','please select an option') 
   else:
      searched_member=database.search(searchcombobox.get(),searchEntry.get())
      tree3.delete(*tree3.get_children())
      for member in searched_member:
          tree3.insert('',END,values=member)   
          
def showall_member():
   treeview_data()   
   searchEntry.delete(0,END)        
   searchcombobox.set('Search By')   
   
def clear():
    userIdEntry.delete(0,END)
    usernameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    latryamountEntry.delete(0,END)
    installmentEntry.delete(0,END)
   
   
def selection1(event):
    global installment
    selected_item = tree2.selection()
    if selected_item:
        row = tree2.item(selected_item)['values']
        clear()
        userIdEntry.insert(0, row[0])
        usernameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        latryamountEntry.insert(0, row[3])
       
        
        # Convert to float after cleaning data
        amount = float(row[3])
        interest = float(row[4].replace('%', '')) # Remove '%' before conversion
        duration = float(row[5]) 
        # Calculate installment
        installment = (amount * interest* (duration/12) / 100)        
        installment=(amount+installment)/duration 
        new_amount=amount-(amount/duration)
       
        print( new_amount)
        installmentEntry.insert(0, math.ceil(installment))# Always rounds up to the next integer
        new_duration = duration - 1

        database.update_amount_and_duration(row[0], new_amount, new_duration)
   
      
def treeview_data():
   members=database.fatch_Uplatryjma()
   tree3.delete(*tree3.get_children())
   for member in members:
      tree3.insert('',END,values=member)  
      
def treeview_data2():
   members=database.fatch_Uplatry()
   tree2.delete(*tree2.get_children())
   for member in members:
      tree2.insert('',END,values=member)   
      
      
         
def new_member():
   clear()
   tree3.selection_remove(tree3.focus())
# def find_installment():
      
         
def Uplatryjma():
   if userIdEntry.get()==''or usernameEntry.get()==''or phoneEntry.get()==''or latryamountEntry.get()==''or installmentEntry.get()=='':
      messagebox.showerror("error","all field are required")
   elif database.id_exists1(userIdEntry.get()):
      messagebox.showerror('error','Id alordy is exists')
   else: 
     database.insert3(userIdEntry.get(),usernameEntry.get(),phoneEntry.get(),latryamountEntry.get(),installmentEntry.get())
     user_id = userIdEntry.get()

     treeview_data2()
     clear()
    
def Storedata():
    result=messagebox.askyesno('Confire','Have you collected all latry members latry then click "Yes" otherwise click "No ')
    if result:
         database.copyupjamalatry()
         database.deleteall2()
            
         treeview_data2()
 
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
phonelable=CTkLabel(liftFrame,text='Phone_no',font=('Goudy Old Style ',15,'bold'))
phonelable.grid(row=2,column=0,padx=20,pady=10,sticky='w')
phoneEntry=CTkEntry(liftFrame,placeholder_text='Enter user phone',width=250)
phoneEntry.grid(row=2,column=1)
latryamountlable=CTkLabel(liftFrame,text='Amount',font=('Goudy Old Style ',15,'bold'))
latryamountlable.grid(row=3,column=0,padx=20,pady=10,sticky='w')
latryamountEntry=CTkEntry(liftFrame,placeholder_text='Enter latryAmount',width=250)
latryamountEntry.grid(row=3,column=1)
installmentlable=CTkLabel(liftFrame,text='installment',font=('Goudy Old Style ',15,'bold'))
installmentlable.grid(row=4,column=0,padx=20,pady=10,sticky='w')
installmentEntry=CTkEntry(liftFrame,placeholder_text='Enter installment',width=250)
installmentEntry.grid(row=4,column=1)


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
tree3 = ttk.Treeview(rightFrame, columns=('Id', 'Username','Phone_no', 'Amount', 'Installment','Date'), 
                    show='headings', height=10)
tree3.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL,command=tree3.yview )
scrollbar.grid(row=1, column=4,sticky='ns')

scrollbar = ttk.Scrollbar(rightFrame, orient=HORIZONTAL, command=tree3.xview)
scrollbar.grid(row=2, column=0, columnspan=4, sticky="ew")

# Define column headings
tree3.heading('Id', text='User ID')
tree3.heading('Username', text='Username')
tree3.heading('Phone_no', text='Phone No')
tree3.heading('Amount', text='Amount')
tree3.heading('Installment', text='Installment')
tree3.heading('Date', text='Date')

# Set column widths (adjusted)
tree3.column('Id', width=50, anchor='center')
tree3.column('Username', width=100, anchor='w')
tree3.column('Phone_no', width=100, anchor='center')
tree3.column('Amount', width=100, anchor='center')
tree3.column('Installment', width=100, anchor='w')
tree3.column('Date', width=150, anchor='w')
treeview_data()



buttonframe=CTkFrame(root)
buttonframe.grid(row=2,column=0,columnspan=2)
newmemberbutton = CTkButton(buttonframe, text='New member',  width=150,command=new_member)
newmemberbutton.grid(row=0, column=0, padx=5, pady=5)
jamalatrybutton = CTkButton(buttonframe, text='Uplatry',  width=150,command=Uplatryjma)
jamalatrybutton.grid(row=0, column=1, padx=5, pady=5)
Storedatabutton = CTkButton(buttonframe, text='Storedata',  width=150,command=Storedata)
Storedatabutton.grid(row=0, column=2, padx=5, pady=5)
jamaentryFrame = CTkFrame(root, height=170, width=800)
jamaentryFrame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
#new treeview for show jamalatry
tree2 = ttk.Treeview(jamaentryFrame, columns=('Id', 'Username',  'Phone_no', 'Amount','Intrest_ret','month_duration','Date'), 
                    show='headings', height=10)
tree2.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

scrollbar = ttk.Scrollbar(jamaentryFrame, orient=VERTICAL,command=tree3.yview )
scrollbar.grid(row=1, column=4,sticky='ns')

scrollbar = ttk.Scrollbar(jamaentryFrame, orient=HORIZONTAL, command=tree3.xview)
scrollbar.grid(row=2, column=0, columnspan=4, sticky="ew")

# Define column headings
tree2.heading('Id', text='User ID')
tree2.heading('Username', text='Username')
tree2.heading('Phone_no', text='Phone No')
tree2.heading('Amount', text='Amount')
tree2.heading('Intrest_ret', text='Intrest_ret')
tree2.heading('month_duration', text='month_duration')
tree2.heading('Date', text='Date')
# Set column widths (adjusted)
tree2.column('Id', width=50, anchor='center')
tree2.column('Username', width=100, anchor='w')
tree2.column('Phone_no', width=100, anchor='center')
tree2.column('Amount', width=100, anchor='w')
tree2.column('Intrest_ret', width=100, anchor='w')
tree2.column('month_duration', width=100, anchor='w')
tree2.column('Date', width=150, anchor='w')
treeview_data2()


root.bind('<ButtonRelease>',selection1)
root.mainloop()
