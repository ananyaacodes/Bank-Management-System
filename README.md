<div align="center">

# 🏦 Bank Management System

### A console-based banking simulator with a real Excel database backend

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Openpyxl](https://img.shields.io/badge/Excel-openpyxl-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://openpyxl.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#license)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)](#)

**[🐛 Report Bug](../../issues) · [💡 Request Feature](../../issues)**

</div>

---

## 📖 Overview

This started as a simple 1st year project — a menu-driven bank simulator that ran entirely in memory and forgot everything the moment you closed it. This version rebuilds it properly: **real persistence, clean architecture, and rules that actually get enforced.**

Every account, deposit, withdrawal, and transfer is written straight into an Excel workbook (`bank_data.xlsx`) that you can open and inspect at any time — no import/export step needed. 🗂️

---

## ✨ Key Features

- 🧾 **Persistent Excel Database** — accounts and transactions live in `bank_data.xlsx`, split across two sheets, and survive across every run
- 🏗️ **Three-layer architecture** — UI (`main.py`), business rules (`bank.py`), and data access (`database.py`) are fully separated
- 💰 **Core banking operations** — create account, deposit, withdraw, transfer funds, close account
- 📜 **Full transaction history** — every action logged with timestamp, type, amount, and running balance
- 🔒 **Validation & guardrails** — minimum opening balance, 18+ age requirement, phone number format checks, guardian approval for minors
- ⚠️ **Proper error handling** — custom exceptions (`InsufficientFundsError`, `AccountNotFoundError`, etc.) instead of silent failures
- 📱 **Phone number management** — change or link multiple numbers per account

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.10+ |
| Storage | Excel (`.xlsx`) via `openpyxl` |
| Interface | Command-line (menu-driven) |

---

## 📂 Project Structure

```
bank_management/
├── main.py          # 🖥️  Menu — the file you run
├── bank.py          # ⚙️  Business rules & validation
├── database.py      # 🗄️  Reads/writes bank_data.xlsx
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/ananyaacodes/Bank-Management-System.git
cd Bank-Management-System

# 2. Install the one dependency
pip install openpyxl

# 3. Run it
python3 main.py
```

`bank_data.xlsx` is created automatically on first run, right next to the script.

---

## 📋 Menu

| # | Option | # | Option |
|---|---|---|---|
| 1 | About | 7 | Transfer Funds |
| 2 | Create Account | 8 | View Account Details |
| 3 | Deposit | 9 | Close Account |
| 4 | Withdraw | 10 | View All Accounts |
| 5 | Check Balance | 11 | Change/Link Phone Numbers |
| 6 | Display Transactions | 12 | Exit |

---

## 🔮 Roadmap

- [ ] PIN-based login per account
- [ ] GUI (Tkinter/PyQt) on top of the existing `bank.py` logic
- [ ] Unit tests with `pytest`
- [ ] Optional SQLite backend as an alternative to Excel

---

## 📄 License

Distributed under the MIT License.