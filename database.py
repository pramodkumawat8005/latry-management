import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor,conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='Shiv#8005',port=3306)
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'Something went wrong. Please ensure MySQL is running before executing.')
        return
    
    # Create database and use it
    mycursor.execute('CREATE DATABASE IF NOT EXISTS MY_LATRY')
    mycursor.execute('USE MY_LATRY')

    # Create table with correct syntax
    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS member (
            userId VARCHAR(20) PRIMARY KEY,
            username VARCHAR(120),
            email VARCHAR(120),
            phone_no VARCHAR(40),
            adhar_no VARCHAR(40),
            address VARCHAR(150)
            
        )
    ''')
    conn.commit()
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS jamalatry (
        userId VARCHAR(20) PRIMARY KEY,
        username VARCHAR(120),
        phone_no VARCHAR(40),
        Amount DECIMAL(10,2),
        late_charge DECIMAL(10,2),
        Total DECIMAL(10,2) NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
    conn.commit()
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Uplatry (
        userId VARCHAR(20) PRIMARY KEY,
        username VARCHAR(120),
        phone_no VARCHAR(40),
        Amount DECIMAL(10,2),
        Intrest_ret VARCHAR(20),
        Month_duration INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
    conn.commit()    
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Uplatryjma (
        userId VARCHAR(20) PRIMARY KEY,
        username VARCHAR(120),
        phone_no VARCHAR(40),
        Amount DECIMAL(10,2),
        Installment VARCHAR(20),
        
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
    conn.commit()        
table_name = None  # Declare globally at the top

def copyjamalatry():
    global table_name  # Ensure we modify the global variable

    mycursor.execute('''CREATE TABLE IF NOT EXISTS copy_tracker (
        id INT PRIMARY KEY AUTO_INCREMENT,
        last_copied_index INT NOT NULL
    )''')
    conn.commit()

    mycursor.execute("SELECT last_copied_index FROM copy_tracker ORDER BY id DESC LIMIT 1")
    result = mycursor.fetchone()
    
    if result:
        last_index = result[0]
    else:
        last_index = 0
        mycursor.execute("INSERT INTO copy_tracker (last_copied_index) VALUES (0)")
        conn.commit()

    new_index = last_index + 1  
    if new_index > 6:  # Fix incorrect limit message (6 copies, not 25)
        print("All 6 copies have already been created.")
        return

    table_name = f"jamalatry_copy{new_index}"  # Store table name globally
    print(f"Using table: {table_name}")

    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} LIKE jamalatry")
    mycursor.execute(f"INSERT INTO {table_name} SELECT * FROM jamalatry")
    conn.commit()

    mycursor.execute("UPDATE copy_tracker SET last_copied_index = %s", (new_index,))
    conn.commit()

def get_last_table_name1():
    """Fetch the last copied table name from the database"""
    mycursor.execute("SELECT last_copied_index FROM copy_tracker ORDER BY id DESC LIMIT 1")
    result = mycursor.fetchone()
    
    if result:
        return f"jamalatry_copy{result[0]}"
    else:
        return None  # No copies exist yet


def copyupjamalatry():
    global table_name  # Ensure we modify the global variable

    mycursor.execute('''CREATE TABLE IF NOT EXISTS copy_tracker1 (
        id INT PRIMARY KEY AUTO_INCREMENT,
        last_copied_index INT NOT NULL
    )''')
    conn.commit()

    mycursor.execute("SELECT last_copied_index FROM copy_tracker1 ORDER BY id DESC LIMIT 1")
    result = mycursor.fetchone()
    
    if result:
        last_index = result[0]
    else:
        last_index = 0
        mycursor.execute("INSERT INTO copy_tracker1 (last_copied_index) VALUES (0)")
        conn.commit()

    new_index = last_index + 1  
    if new_index > 6:  # Fix incorrect limit message (6 copies, not 25)
        print("All 6 copies have already been created.")
        return

    table_name = f"upjamalatry_copy{new_index}"  # Store table name globally
    print(f"Using table: {table_name}")

    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} LIKE uplatryjma")
    mycursor.execute(f"INSERT INTO {table_name} SELECT * FROM uplatryjma")
    conn.commit()

    mycursor.execute("UPDATE copy_tracker1 SET last_copied_index = %s", (new_index,))
    conn.commit()

def get_last_table_name():
    """Fetch the last copied table name from the database"""
    mycursor.execute("SELECT last_copied_index FROM copy_tracker1 ORDER BY id DESC LIMIT 1")
    result = mycursor.fetchone()
    
    if result:
        return f"upjamalatry_copy{result[0]}"
    else:
        return None  # No copies exist yet

import decimal

def findTotal(userId, Amount, charge):
    global table_name

    if not table_name:  # If table_name is not set, retrieve from DB
        table_name = get_last_table_name1()  # Make sure this is the jamalatry one

    if not table_name:  
        print("Error: Table name is not defined! Call copyjamalatry() first.")
        return None

    query = f"SELECT Total FROM {table_name} WHERE userId = %s"
    mycursor.execute(query, (userId,))
    result = mycursor.fetchone()

    if result is None:
        print(f"Error: User ID {userId} not found in the table.")
        return None

    current_total = result[0]
    
    Amount = decimal.Decimal(str(Amount))
    charge = decimal.Decimal(str(charge))
    new_total = current_total + Amount + charge

    return new_total


    


def get_total_amount():
    global table_name

    if not table_name: 
        table_name = get_last_table_name1()  # Make sure this is the jamalatry one

    if not table_name:  
        print("Error: Table name is not defined! Call copyjamalatry() first.")
        return None
    try:
      
        mycursor.execute(f"SELECT SUM(Total) FROM {table_name}")
        result = mycursor.fetchone()

        total_amount = result[0] if result[0] is not None else 0
        return total_amount

   
    finally:
        if mycursor:
            mycursor.close()
        if conn:
            conn.close()

    

def insert(userId, username, email,phone_no,  adhar_no, address):
    try:
        query = "INSERT INTO member (userId, username,  email,phone_no, adhar_no, address) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (userId, username,  email,phone_no, adhar_no, address)
        mycursor.execute(query, values)
        conn.commit()
        messagebox.showinfo('Success', 'Member added successfully!')
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong: {e}')
        
def insert1(userId, username, phone_no, Amount,late_charge,Total):
    try:
        query = "INSERT INTO jamalatry (userId, username, phone_no, Amount,late_charge,Total) VALUES (%s,%s, %s, %s, %s, %s)"
        values = (userId, username,phone_no,Amount,late_charge,Total)
        mycursor.execute(query, values)
        conn.commit()
        messagebox.showinfo('Success', 'Member added successfully!')
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong: {e}') 

def insert2(userId, username, phone_no, Amount,Intrest_ret,Month_duration):
    try:
        query = "INSERT INTO Uplatry (userId, username, phone_no, Amount,Intrest_ret,Month_duration) VALUES (%s, %s, %s, %s, %s,%s)"
        values = (userId, username,phone_no,Amount,Intrest_ret,Month_duration)
        mycursor.execute(query, values)
        conn.commit()
        messagebox.showinfo('Success', 'Member added successfully!')
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong: {e}') 
def insert3(userId, username, phone_no, Amount,Installment):
    try:
        query = "INSERT INTO Uplatryjma (userId, username, phone_no, Amount,Installment) VALUES (%s, %s, %s, %s,%s)"
        values = (userId, username,phone_no,Amount,Installment)
        mycursor.execute(query, values)
        conn.commit()
        messagebox.showinfo('Success', 'Member added successfully!')
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong: {e}')                               
def id_exists(userId):
    mycursor.execute('SELECT COUNT(*) FROM member WHERE userId=%s', (userId,))
    result=mycursor.fetchone()
    return result[0]>0 

def id_exists1(userId):
    mycursor.execute('SELECT COUNT(*) FROM jamalatry WHERE userId=%s', (userId,))
    result=mycursor.fetchone()
    return result[0]>0 
def id_exists2(userId):
    mycursor.execute('SELECT COUNT(*) FROM Uplatry WHERE userId=%s', (userId,))
    result=mycursor.fetchone()
    return result[0]>0  
def id_exists3(userId):
    mycursor.execute('SELECT COUNT(*) FROM Uplatryjma WHERE userId=%s', (userId,))
    result=mycursor.fetchone()
    return result[0]>0  
def fatch_member():
    mycursor.execute('SELECT * FROM member ORDER BY CAST(userId AS UNSIGNED)')
    result = mycursor.fetchall()
    return result
def fatch_jamalatry():
    mycursor.execute('SELECT * FROM jamalatry ORDER BY CAST(userId AS UNSIGNED)')
    result = mycursor.fetchall()
    return result
def fatch_Uplatry():
    mycursor.execute('SELECT * FROM Uplatry ORDER BY CAST(userId AS UNSIGNED)')
    result = mycursor.fetchall()
    return result
def fatch_Uplatryjma():
    mycursor.execute('SELECT * FROM Uplatryjma ORDER BY CAST(userId AS UNSIGNED)')
    result = mycursor.fetchall()
    return result
def update(userId, new_username,  new_email,new_phone_no, new_adhar_no, new_address):
         mycursor.execute('UPDATE member SET username=%s,  email=%s,phone_no=%s, adhar_no=%s, address=%s WHERE userId=%s',(new_username,  new_email,new_phone_no, new_adhar_no, new_address,userId,))
         conn.commit()
# database.py
def update_amount_and_duration(user_id, new_amount, new_month_duration):
    query = '''
        UPDATE Uplatry
        SET Amount = %s,
            Month_duration = %s
        WHERE userId = %s
    '''
    values = (new_amount, new_month_duration, user_id)
    mycursor.execute(query, values)
    conn.commit()


             
def delete(userId):
    mycursor.execute('DELETE FROM member WHERE userId=%s',userId) 
    conn.commit()
def search(option, value):
    mycursor.execute(f"SELECT * FROM member WHERE {option}=%s",value)    
    result=mycursor.fetchall()
    return result
def deleteall():
    mycursor.execute('TRUNCATE TABLE member')
    conn.commit()
def deleteall1():
    mycursor.execute('TRUNCATE TABLE jamalatry')
    conn.commit()    
def deleteall2():
    mycursor.execute('TRUNCATE TABLE uplatryjma')
    conn.commit() 
connect_database()        
