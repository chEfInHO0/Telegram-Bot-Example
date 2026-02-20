# 🤖 Telegram Bot — Python Template

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-21.5-blue?logo=telegram)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A modular, production-ready Telegram bot template built with Python. Designed to be a solid starting point for bots that need structured logging, access control, time-based restrictions, and clean project organization.

---

## ✨ Features

- 🔐 **User authorization** — only whitelisted Telegram IDs can access protected commands
- 🕐 **Time-based restrictions** — commands can be automatically blocked outside business hours
- 📋 **Structured logging** — separate log files for debug, info, warnings, and errors
- 📦 **Modular architecture** — each concern (auth, logging, alerts) is isolated in its own module
- 🔒 **Secure by default** — sensitive data loaded via `.env`, never hardcoded

---

## 📁 Project Structure

```
├── main.py                  # Entry point — bot setup and command registration
├── BlockBot/
│   └── main.py              # Time-based access control logic
├── Logs/
│   └── main.py              # Logger factory (debug, info, warning, error)
├── Utils/
│   ├── alert.py             # Console alert utility (info, warning, critical)
│   └── errorRaiser.py       # Centralized error handling helpers
├── .env.example             # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- A Telegram bot token (see [Creating a bot](#-creating-a-telegram-bot) below)

### 1. Clone the repository

```bash
git clone https://github.com/chEfInHO0/Telegram-Bot-Example.git
cd Telegram-Bot-Example
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows:**

```powershell
.\venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```env
TOKEN=your_telegram_bot_token_here
BOT_USERNAME=@your_bot_username
AUTH_GRANTED=[123456789, 987654321]
```

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

### 5. Run the bot

```bash
python main.py
```

---

## 🤖 Available Commands

| Command  | Description                         | Authorization required |
| -------- | ----------------------------------- | ---------------------- |
| `/start` | Greets the user                     | No                     |
| `/ping`  | Health check — responds with `Pong` | No                     |
| `/test`  | Basic test command                  | No                     |

---

## 🔐 Access Control

User authorization is handled by checking the sender's Telegram ID against the `AUTH_GRANTED` list defined in `.env`.

To find your Telegram user ID, you can use [@userinfobot](https://t.me/userinfobot).

---

## 🕐 Time-Based Restrictions (BlockBot)

The `BlockBot` module allows commands to be automatically disabled after a configured time. By default, protected commands are blocked after **17:30**.

```python
# BlockBot/main.py
def blockbot():
    limit = datetime(YEAR, MONTH, DAY, hour=17, minute=30)
    return datetime.today() > limit
```

To change the cutoff time, edit the `HOUR` and `MINUTE` constants in `BlockBot/main.py`.

---

## 📋 Logging

The `Logs` module provides a logger factory that creates isolated loggers, each writing to its own file:

| Logger            | File           | Level   |
| ----------------- | -------------- | ------- |
| `debugger.logger` | `debug.log`    | DEBUG   |
| `command_logger`  | `commands.log` | INFO    |
| `warning_logger`  | `warnings.log` | WARNING |
| `error_logger`    | `errors.log`   | ERROR   |

Log files are stored inside the `Logs/` directory and are excluded from version control via `.gitignore`.

---

## 🔔 Console Alerts

The `Alert` utility provides colored console output for startup warnings:

```python
from Utils.alert import Alert

Alert("Check your .env file before running", "warning").display()
Alert("TOKEN is missing!", "critical").display()
```

---

## 🛠️ Extending the Bot

To add a new command:

```python
# 1. Define the handler in main.py
async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")

# 2. Register it in the main() function
app.add_handler(CommandHandler('hello', hello_command))
```

---

## 📦 Dependencies

| Package               | Version | Purpose                  |
| --------------------- | ------- | ------------------------ |
| `python-telegram-bot` | 21.5    | Telegram Bot API wrapper |
| `python-dotenv`       | 1.0.1   | `.env` file loading      |
| `httpx`               | 0.27.2  | Async HTTP client        |

---

## 🤖 Creating a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the instructions
3. Copy the token provided and paste it into your `.env` file as `TOKEN`

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Luccas Elias de Almeida dos Santos**  
[GitHub](https://github.com/chEfInHO0) · [LinkedIn](https://linkedin.com/in/luccas-santos-3a86b31a6/)
