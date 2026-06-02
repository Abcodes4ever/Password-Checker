# 🔐 Password Strength Checker

A modern desktop application built with **Python Tkinter** that analyzes password strength in real time and provides feedback to help users create secure passwords.

## 📌 Features

* ✅ Real-time password strength analysis
* ✅ Password visibility toggle (Show/Hide Password)
* ✅ Strength classification:

  * Very Weak
  * Weak
  * Medium
  * Strong
  * Very Strong
* ✅ Password entropy calculation
* ✅ Visual strength meter with color-coded progress bar
* ✅ Password requirement checklist
* ✅ Instant feedback and recommendations
* ✅ Responsive GUI built with Tkinter

## 🖥️ Preview

The application evaluates passwords based on:

* Minimum length (12+ characters)
* Uppercase letters (A-Z)
* Lowercase letters (a-z)
* Numbers (0-9)
* Special characters (!@#$%^&*)

It also calculates password entropy to estimate resistance against brute-force attacks.

## 📂 Project Structure

```text
password-strength-checker/
│
├── password_strength_checker.py
├── README.md
```

## 🚀 Installation

### Prerequisites

* Python 3.8 or higher

### Clone the Repository

```bash
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker
```

### Run the Application

```bash
python password_strength_checker.py
```

## 🛠️ Technologies Used

* Python
* Tkinter
* ttk (Themed Tkinter Widgets)
* Regular Expressions (`re`)
* Mathematics Module (`math`)

## 📊 Strength Evaluation Criteria

| Requirement       | Points   |
| ----------------- | -------- |
| 12+ Characters    | 25       |
| Uppercase Letter  | 15       |
| Lowercase Letter  | 15       |
| Number            | 15       |
| Special Character | 20       |
| Entropy Bonus     | Up to 25 |

### Password Ratings

| Score Range | Strength    |
| ----------- | ----------- |
| < 40        | Very Weak   |
| 40 - 59     | Weak        |
| 60 - 79     | Medium      |
| 80 - 99     | Strong      |
| 100+        | Very Strong |

## 🔒 Entropy Calculation

Password entropy is calculated using:

```text
Entropy = Password Length × log₂(Character Set Size)
```

Higher entropy indicates a stronger and more secure password.

## 🎯 Example Passwords

| Password         | Rating      |
| ---------------- | ----------- |
| password123      | Weak        |
| MyPassword2025   | Medium      |
| MyP@ssword2025!  | Strong      |
| V7#kP2!mQ9$zL4@x | Very Strong |

## 📸 Key Features

* Live password validation
* Dynamic strength indicator
* Entropy measurement
* Requirement checklist
* User-friendly interface
* Password visibility control

## 🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the **No License** model.

All rights are reserved by the author. No permission is granted to use, modify, distribute, or sublicense this software without explicit permission from the author.

## 👨‍💻 Author

Developed using Python and Tkinter as a desktop cybersecurity utility for password strength assessment.
