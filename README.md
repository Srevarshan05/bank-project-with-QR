# 🏦 Console-based Python Banking System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Project-Completed-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A structured **banking system simulation built using Python** that demonstrates core financial operations along with transaction verification and QR-based transaction records.

This project implements essential banking features such as **deposit, withdrawal, balance inquiry, OTP authentication, and QR code generation** for transaction verification. The system focuses on showcasing how secure transaction workflows can be implemented in a Python-based application.

---

# 📌 Project Overview

The **Python Banking System** simulates real-world banking operations through a command-line interface. It allows users to perform common financial actions while ensuring that transactions are validated through **OTP authentication**.

After every successful transaction, the system generates a **QR code containing the transaction details**, allowing the user to retrieve the information later by scanning the QR code.

This project is designed as a learning implementation of:

- Transaction-based application design
- Basic security verification using OTP
- QR code generation and encoding
- Python-based system logic

---

# ⚙️ Core Features

## 💰 Deposit Funds
- Allows users to deposit money into their account.
- Updates the account balance instantly.
- Maintains accurate transaction records.

## 💳 Withdraw Funds
- Enables withdrawal of funds from the account.
- Ensures sufficient balance before completing the transaction.
- Prevents invalid withdrawal attempts.

## 📊 Balance Inquiry
- Displays the current account balance.
- Provides a quick overview of available funds.

## 🔐 OTP Transaction Verification
- Adds an additional layer of security.
- Generates a **One-Time Password (OTP)** for transaction validation.
- Ensures that only authorized transactions are executed.

## 📱 QR Code Generation
- Automatically generates a **QR code after every transaction**.
- Encodes transaction details securely.
- Allows easy retrieval of transaction information by scanning the QR code.

---

# 🧠 System Workflow

1. User selects a banking operation.
2. Transaction request is initiated.
3. OTP verification is performed.
4. If verification succeeds:
   - Transaction is processed
   - Account balance is updated
5. A QR code containing transaction details is generated.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Core programming language |
| qrcode Library | QR code generation |
| Random / OTP Logic | Transaction verification |
| CLI Interface | User interaction |

---

# 📂 Project Structure

```
Python-Banking-System
│
├── banking_system.py
├── otp_verification.py
├── qr_generator.py
└── README.md
```

---

# 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Srevarshan05/Python-Banking-System.git
```

### 2️⃣ Navigate to Project Directory

```bash
cd Python-Banking-System
```

### 3️⃣ Install Required Dependencies

```bash
pip install qrcode[pil]
```

### 4️⃣ Run the Application

```bash
python banking_system.py
```

---

# 🔒 Security Considerations

This project includes basic transaction security mechanisms such as:

- OTP-based transaction verification
- Controlled account balance updates
- Encoded transaction records through QR codes

While the system is a simulation, it demonstrates how **authentication and verification layers** can be implemented in financial software.

---

# 📈 Possible Future Improvements

Some potential enhancements for this project include:

- GUI-based banking interface
- Database integration for persistent account storage
- User authentication and login system
- Transaction history logging
- Encrypted QR transaction records
- REST API integration for banking services

---

# 📖 Learning Outcomes

This project demonstrates practical understanding of:

- Python application development
- Transaction logic implementation
- Secure verification workflows
- QR code data encoding
- Structuring command-line applications

---

# 👨‍💻 Author

**Srevarshan**

AI & Software Developer

GitHub:  
https://github.com/Srevarshan05

---

⭐ If you found this project useful, consider giving it a star on GitHub.
