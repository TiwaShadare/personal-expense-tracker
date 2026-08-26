# personal-expense-tracker
A simple Python application for tracking personal expenses.
# Personal Expense Tracker

A simple command-line application built with Python for tracking personal expenses.

## Project Overview

The Personal Expense Tracker allows users to record their expenses, organize them by category, view their recorded expenses, and calculate their total spending.

This project was created as a small practical application to demonstrate Python programming fundamentals and basic data management.

## Features

* Add a new expense
* Enter an expense name
* Enter an expense amount
* Assign an expense category
* View all recorded expenses
* Calculate total spending
* Simple command-line interface
* Basic input validation

## Technologies Used

* Python 3
* Python Lists
* Python Dictionaries
* Functions
* Loops
* Conditional Statements
* User Input

## Project Structure

```text
personal-expense-tracker/
│
├── expense_tracker.py
├── sample_expenses.txt
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Download or Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/personal-expense-tracker.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 3. Open the Project Folder

```bash
cd personal-expense-tracker
```

### 4. Run the Application

```bash
python expense_tracker.py
```

## How to Use

After starting the application, you will see the following menu:

```text
==============================
      PERSONAL EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. View Total
4. Exit
```

### Add an Expense

Select option `1`.

Enter:

* Expense name
* Amount
* Category

Example:

```text
Enter expense name: Groceries
Enter amount: $85
Enter category: Food

Expense added successfully!
```

### View Expenses

Select option `2` to see all expenses that have been entered during the current session.

Example:

```text
Your Expenses
---------------------------------------------
Groceries            $   85.00   Food
Gas                  $   45.00   Transportation
Netflix              $   15.99   Entertainment
---------------------------------------------
```

### View Total

Select option `3` to calculate total spending.

Example:

```text
Total spending: $145.99
```

### Exit

Select option `4` to close the application.

## Future Improvements

Potential future improvements include:

* Saving expenses to a CSV or database
* Editing existing expenses
* Deleting expenses
* Searching expenses by category
* Monthly spending summaries
* Budget limits and notifications
* Graphs and spending visualizations
* A web-based user interface

## Learning Objectives

This project demonstrates the use of:

* Python functions
* Lists and dictionaries
* Loops
* Conditional logic
* Exception handling
* User input
* Basic data processing
* GitHub project documentation

## Author

Tiwa

Master's Student — Computer Information Systems and Business Analysis
