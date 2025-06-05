# latry-management

# 🧾 Latry Management System

This is a Python-based desktop application for managing Latry (installment-based) member records. Built with **CustomTkinter**, **MySQL**, and **OOP-based Python**, the system handles installment uploads, member updates, and login authentication efficiently.

---

## 🚀 Features

- 🔐 Login system for admin/company access
- 📥 Add and update member installments
- 🔍 Search members and view records
- 📊 Calculate and show total amounts
- 💾 Store data in MySQL database
- 🧩 Modular structure using OOP in Python

---

## 🛠️ Technologies Used

- **Frontend**: Python + CustomTkinter
- **Backend**: Python Classes + Functions
- **Database**: MySQL
- **Library**: `tkinter`, `customtkinter`, `mysql.connector`, `datetime`

---

## 📁 Project Structure

latry-management/
│
├── JamaUp_latry.py # Upload new installment entries
├── login.py # Login interface and validation
├── up_latry.py # Update existing member records
├── database/ # (Optional) MySQL connection and schema
└── README.md # Project overview (this file)

yaml
Copy
Edit

---

## ⚙️ How to Run

1. **Install dependencies**:
   ```bash
   pip install customtkinter mysql-connector-python
Set up MySQL database:

Create a database (e.g., latry_db)

Create necessary tables (members, installments)

Update database credentials inside Python files:

python
Copy
Edit
mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="latry_db"
)
Run the login file to start the app:

bash
Copy
Edit
python login.py
🧩 Future Enhancements
PDF report generation

Member payment history view

Export to Excel

Mobile version using Kivy or Flutter

👨‍💻 Author
Pramod Kumawat
📧 [Email (optional)]
🌐 [Shine / GitHub / LinkedIn link if you want]
