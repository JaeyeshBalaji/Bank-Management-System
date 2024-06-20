# Bank-Management-System

This repository contains the source code for a Bank Management System built using Python. The system provides functionalities to create, view, update, and delete bank accounts with various details such as Aadhar number, name, mobile number, email, age, gender, address, and date of birth. Additionally, it supports money deposit, withdrawal, and viewing account balance using the Aadhar number.

## Features

- **Create New Bank Accounts**: 
  - Enter user details in the provided fields and click the submit button to create a new bank account. 
  - A minimum balance of 1000 is deposited during account creation.

- **View Account Details (Sorted and Unsorted)**: 
  - Choose to view accounts either sorted or unsorted.

- **Update Existing Accounts**: 
  - Enter the Aadhar number of the account to be updated.
  - Provide the new details.

- **Delete Accounts**: 
  - Enter the Aadhar number of the account to be deleted.
  - To delete all accounts, enter 100.

- **Money Deposit and Withdraw**: 
  - The account balance cannot go below 1000.
  - Money can be deposited and withdrawn using the Aadhar number.

- **View Account Balance**: 
  - Account balance can be viewed using the Aadhar number.

- **Exit**


## Requirements

The project requires MySQL along with the following Python libraries, as specified in the `requirements.txt` file:

mysql-connector-python
tkcalendar

## Getting Started

### Prerequisites

    Python 3.x
    MySQL Server

### Installation

#### 1. Clone this repository to your local machine:

 ```sh   
git clone https://github.com/JaeyeshBalaji/Bank-Management-System.git
cd Bank-Management-System
```

#### 2. Install the required libraries:

```sh
pip install -r requirements.txt
```
#### 3. Update the MySQL connection details in the code as per your MySQL server configuration:

```sh
con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
```

These are default settings in source code. If you have different settings then change source code accordingly.

### Running the Application

Run the main script to start the application:

```sh
python main_code.py
```
