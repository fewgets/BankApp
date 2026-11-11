<!-- BankApp · README by Usama Shahid (fewgets) -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,55:0F3D3E,100:36FFC7&height=230&section=header&text=BankApp&fontSize=60&fontColor=FFFFFF&fontAlignY=36&desc=Desktop%20banking%20system%20on%20Supabase&descSize=17&descAlignY=58&animation=fadeIn" width="100%" alt="BankApp"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=700&color=36FFC7&center=true&vCenter=true&width=720&height=60&lines=Sign+Up%2C+Log+In%2C+Transact;CustomTkinter+%2B+Supabase;Balances%2C+PINs+and+Statements" alt="Typing SVG"/>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/CustomTkinter-1F6FEB?style=for-the-badge&logo=python&logoColor=white" alt="CustomTkinter"/>
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
</p>

</div>

---
## 📌 Overview

**BankApp** is a desktop banking application built with **Python** and **CustomTkinter**, with
**Supabase (PostgreSQL)** as the cloud backend. Users can open an account, log in, check their
balance, transfer money, pay bills, manage their card PIN and view their transaction history,
all from a clean, modern desktop interface.

---

## 📷 Screenshots

| Login | Sign Up |
|:-:|:-:|
| ![Login](screenshots/login.png) | ![Sign Up](screenshots/signup.png) |
| **Dashboard** | **Transaction History** |
| ![Dashboard](screenshots/main_page.png) | ![Transactions](screenshots/transaction.png) |

---

## ✨ Features

| | Feature | Description |
|:-:|---|---|
| 🔐 | **Sign Up & Login** | Account creation and secure login |
| 🔑 | **Forgot Password** | Recover access to an account |
| 💰 | **Balance Management** | Live balance stored in the cloud |
| 💸 | **Transfers & Bill Payments** | Move money and pay bills from the dashboard |
| 💳 | **Card PIN Management** | Change your card PIN at any time |
| 📜 | **Mini Statement** | Full transaction history |
| ☁️ | **Supabase Backend** | All data stored in PostgreSQL via the Supabase API |

---

## 🏗️ Architecture

```mermaid
flowchart LR
    U[👤 User] --> UI[🖥️ CustomTkinter UI<br/>start · login · signup · dashboard]
    UI --> DB[⚙️ Database.py<br/>CRUD logic]
    DB --> S[(☁️ Supabase<br/>PostgreSQL)]
```

| File | Responsibility |
|---|---|
| `main.py` / `start.py` | App entry and the start screen (login or sign up) |
| `login_page.py` · `signup_page.py` · `forgot_password.py` | Authentication screens |
| `first_page.py` | Account dashboard |
| `Database.py` | All Supabase operations |
| `config.py` | Supabase URL and key (you fill these in) |
| `sql_queries.txt` | Database schema |

---

## 🚀 Run Locally

### 1. Clone and install

```bash
git clone https://github.com/fewgets/BankApp.git
cd BankApp
pip install customtkinter supabase pillow
```

### 2. Set up Supabase

1. Create a free project at [supabase.com](https://supabase.com).
2. Open **SQL Editor**, paste the contents of `sql_queries.txt` and run it. This creates the `users`, `transaction` and `card_management` tables.
3. Add your project credentials to `config.py`:

```python
url = "https://your-project.supabase.co"
key = "your-supabase-anon-key"
```

### 3. Start the app

```bash
python main.py
```

---

## 🛡️ Notes

- New accounts start with a demo balance of **10,000** and a default PIN of **0000**. Change it after the first login.
- Never commit real Supabase keys. Keep `config.py` local.

---

## 🧰 Tech Stack

| Component | Tool |
|---|---|
| Language | Python 3 |
| UI | CustomTkinter, Pillow |
| Backend | Supabase (PostgreSQL) via `supabase-py` |

---

## 🤝 Let's Work Together

<div align="center">

**Have an idea, a freelance project, or want to collaborate on something in AI?**
I'm always open to collaborations, freelance work and full-time opportunities.

<a href="mailto:shaikhusama541@gmail.com?subject=Collaboration%20-%20BankApp">
  <img src="https://img.shields.io/badge/Email-shaikhusama541%40gmail.com-36FFC7?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117" alt="Email"/>
</a>
<a href="https://www.linkedin.com/in/-usamashahid/">
  <img src="https://img.shields.io/badge/LinkedIn-Usama%20Shahid-36FFC7?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0D1117" alt="LinkedIn"/>
</a>
<a href="https://github.com/fewgets">
  <img src="https://img.shields.io/badge/GitHub-fewgets-36FFC7?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" alt="GitHub"/>
</a>

<br/><br/>

⭐ **If you like this project, please give it a star. It really helps!** ⭐

<br/>

<h3>"Good software makes handling money feel simple."</h3>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:36FFC7,55:0F3D3E,100:0D1117&height=150&section=footer&animation=twinkling" width="100%" alt="footer"/>

</div>
