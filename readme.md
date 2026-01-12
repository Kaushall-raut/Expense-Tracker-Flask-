# Expense Tracker (Flask)

A full-featured **Expense Tracker web application** built using **Python, Flask, and SQLite**.
It allows users to **add, filter, update, delete, visualize, and export expenses** efficiently.

---

## Overview

This Expense Tracker helps users manage daily expenses with practical features such as:

* Date-wise filtering
* Category-wise analysis
* Expense editing and deletion
* CSV export
* Visual charts for insights

This project is ideal for **learning Flask, SQLAlchemy, and backend development**.

---

## Features

### Expense Management

* Add new expenses (description, amount, category, date)
* Edit existing expenses
* Delete expenses

### Filtering & Search

* Filter expenses by:

  * Start date
  * End date
  * Category
* Validation for incorrect date ranges

### Analytics

* Total expense calculation
* Category-wise expense summary
* Date-wise expense chart data

### Export

* Export filtered expenses as **CSV**

### Notifications

* Success and error messages using Flask `flash`

---

## Tech Stack

| Layer    | Technology               |
| -------- | ------------------------ |
| Backend  | Python, Flask            |
| Database | SQLite                   |
| ORM      | SQLAlchemy               |
| Frontend | HTML, CSS, Jinja2        |
| Charts   | Chart.js                 |
| Server   | Flask Development Server |

---

## Project Structure

```
Expense-Tracker-Flask-/
├── app.py
├── templates/
│   ├── index.html
│   ├── edit.html
│   └── base.html
├── instance/
│   └── expense.db
└── README.md
```

---

## Database Schema

### Expense Table

| Column      | Type                  |
| ----------- | --------------------- |
| id          | Integer (Primary Key) |
| description | String                |
| amount      | Float                 |
| category    | String                |
| date        | Date                  |

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/Kaushall-raut/Expense-Tracker-Flask-.git
cd Expense-Tracker-Flask-
```

### Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate
```

### Install Dependencies

```bash
pip install flask flask-sqlalchemy
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000/
```

---

## Usage

* Add expenses using the form
* Filter by date range and category
* Edit or delete records
* Export expenses as CSV
* View totals and charts

---

## Future Enhancements

* User authentication
* Monthly / yearly reports
* Improved charts
* PDF export
* Cloud database support

---

## Author

**Kaushal Raut**
GitHub: [https://github.com/Kaushall-raut](https://github.com/Kaushall-raut)

---

## License

This project is open-source and free to use for **learning and academic purposes**.
