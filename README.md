# 🚀 Trading Bot (Binance Futures Testnet)

A clean, modular Python CLI application to simulate placing MARKET and LIMIT orders on Binance Futures Testnet.

---

## ✨ Features

* ✅ Place MARKET orders
* ✅ Place LIMIT orders
* ✅ CLI-based interaction
* ✅ Input validation (symbol, side, order type, quantity, price)
* ✅ Structured architecture (client / orders / validators)
* ✅ Logging of requests & responses
* ✅ Error handling (invalid input, runtime issues)
* ✅ Clean and readable output

---

## 🧱 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── orders.py          # Order logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── logs/                  # Log files
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### ▶️ MARKET Order

```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

---

### ▶️ LIMIT Order

```bash
python cli.py BTCUSDT BUY LIMIT 0.001 60000
```

---

## 📊 Example Output

```
===== ORDER REQUEST =====
Symbol   : BTCUSDT
Side     : BUY
Type     : LIMIT
Quantity : 0.001
Price    : 60000.0

===== RESPONSE =====
orderId: 274739
symbol: BTCUSDT
status: NEW
type: LIMIT
side: BUY
price: 60000.0
origQty: 0.001

Result: Success ✅
```

---

## 🛡️ Validation Rules

* Side must be: `BUY` or `SELL`
* Order type must be: `MARKET` or `LIMIT`
* Quantity must be > 0
* Price required for LIMIT orders
* Only `USDT` pairs supported

---

## 📝 Logging

* All requests, responses, and errors are logged
* Log file location:

```
logs/trading.log
```

---

## ⚠️ Note on Binance API

Due to recent inconsistencies and access limitations in Binance demo/testnet environments,
order execution is **simulated** to ensure consistent behavior.

👉 The system is designed to easily integrate with real Binance APIs when stable access is available.

---

## 💡 Design Decisions

* Simplified CLI parsing (avoids argument ambiguity)
* Modular structure for scalability
* Separation of concerns (validation, logic, logging)
* Mocked API layer for reliability during testing

---

## 🎯 Future Improvements

* 🔹 Stop-Loss / Take-Profit orders
* 🔹 Retry mechanism for API failures
* 🔹 Real-time price fetching
* 🔹 Enhanced CLI UX (menus / prompts)
* 🔹 Web UI (optional)

---

## 🧑‍💻 Author

**Chaitna Reddy**

---

## ⭐ Final Note

This project demonstrates:

* Clean coding practices
* Real-world debugging ability
* Structured backend design
* Practical CLI application development

---
