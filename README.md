# VOSYS - Secure Voting System

## Project Overview
VOSYS is a secure, modular voting system designed to ensure privacy, integrity, and ease of use for both administrators and voters. It leverages strong encryption, multi-factor authentication, and automated result sharing to deliver a robust election platform.

## Highlights

- **Entire database is encrypted using the RSA cipher.**
- **Uses MySQL as the database.**
- **Provides a user-friendly interface (Tkinter-based GUI).**
- **Validates each person using TOTP (Time-Based One-Time Password).**
- **Automatically shares election results via email.**
- **Guarantees complete voter anonymity.**
- **Includes an Election Integrity Mode to prevent changes during the voting process.**

---



## Features
- **Admin & Voter Panels:** Separate interfaces for administrators and voters.
- **Person & Category Management:** Add, validate, and categorize users securely.
- **Election Management:** Create, update, and monitor elections with integrity controls.
- **Result Sharing:** Election results are sent automatically via email.
- **Security:** All sensitive data is encrypted using RSA; TOTP is used for user validation.

## Technologies Used
- **Python 3.x**
- **Tkinter** (for GUI)
- **MySQL** (database)
- **RSA** (encryption)
- **TOTP** (authentication)
- **Email (SMTP)** (result sharing)

## Setup Instructions
1. **Install Python 3.x**
2. **Install MySQL and create the required database/tables** (see `2. Database Queries/DDL.sql`)
3. **Install required Python packages:**
   - `pyotp`, `qrcode`, `Pillow`, `mysql-connector-python` (or similar)
4. **Run the application:**
   ```bash
   python main.py
   ```

## Usage
- **Admins:** Log in to manage elections, categories, and users.
- **Voters:** Authenticate using CNIC and TOTP to cast votes anonymously.

## Folder Structure
- `Includes/` - Utility classes (encryption, email, TOTP, etc.)
- `Logic/` - Core business logic (Admin, Voter, Elections, etc.)
- `UI/` - User interface components (Admin, Voter, Results, etc.)
- `main.py` - Application entry point

## License
This project is for educational and demonstration purposes.
