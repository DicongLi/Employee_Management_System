Project Overview
The Employee Management System (EMS) is a system designed to manage employee information. This project includes all relevant code and virtual data, constructing a basic employee management interface that provides a user-friendly experience.

Features
Employee Information Management: 
Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask framework)
Database: SQLite (for storing virtual data)

File Structure
```
Employee_Management_System/
│
├── app.py             # Main backend program file
├── templates/         # HTML template files
│   ├── layout.html    # Basic page layout template
│   ├── login.html     # Login page
│   ├── register.html  # Registration page
│   └── dashboard.html # Employee management page
├── static/            # Static files (CSS, JS, images)
├── data/              # Virtual data files
└── README.md          # Project description file
```

Installation and Running
Prerequisites
Ensure your system has the following components installed:
 Python 3.x
 Git

Clone the Repository
```
git clone https://github.com/DicongLi/Employee_Management_System.git
cd Employee_Management_System
```

Install Dependencies
Install the required libraries with the following command:
```
pip install -r requirements.txt
```

Start the Project
Run the following command in the project directory to start the Flask server:
```
python app.py
```

Then open `http://127.0.0.1:5000` in your browser to view the project.

Contribution
We welcome everyone to submit PRs to improve this project! Please make sure all tests pass and that code formatting meets project standards before submitting.
