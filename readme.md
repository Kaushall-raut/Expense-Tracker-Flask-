💰 Expense Tracker – Flask

A full-featured Expense Tracker web application built using Python, Flask, and SQLite.
This application allows users to add, filter, update, delete, visualize, and export expenses efficiently.

📖 Overview

This Expense Tracker helps users manage daily expenses with powerful features like:

Date-wise filtering

Category-wise analysis

Expense editing and deletion

CSV export

Charts for insights

It is ideal for learning Flask, SQLAlchemy, and backend logic with real-world use cases.

✨ Features
🧾 Expense Management

Add new expenses (description, amount, category, date)

Edit existing expenses

Delete expenses

🔍 Filtering & Search

Filter expenses by:

Start date

End date

Category

Validation for incorrect date ranges

📊 Analytics

Total expense calculation

Category-wise expense summary

Date-wise expense chart data

📤 Export

Export filtered expenses as CSV file

🔐 Flash Messages

Success and error messages using Flask flash

🛠️ Tech Stack
Layer	Technology
Backend	Python, Flask
Database	SQLite
ORM	SQLAlchemy
Frontend	HTML, CSS, Jinja2
Charts	Chart.js (via template)
Server	Flask Development Server

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Kaushall-raut/Expense-Tracker-Flask-.git
cd Expense-Tracker-Flask-

2️⃣ Create & Activate Virtual Environment

Windows

python -m venv env
env\Scripts\activate


Mac / Linux

python3 -m venv env
source env/bin/activate

3️⃣ Install Dependencies
pip install flask flask-sqlalchemy


(Or use requirements.txt if available)

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/

🧪 Usage Guide

➕ Add expenses using the form

📅 Filter expenses by date range

🗂 Filter expenses by category

✏️ Edit existing records

🗑 Delete unwanted expenses

📤 Export data as CSV

📊 View analytics via charts

📤 CSV Export Example
expenses_2024-01-01 to 2024-01-31.csv


Contains:

date,description,category,amount