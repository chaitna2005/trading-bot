# Trading Bot (Binance Futures Testnet)

## 📌 Features

* Place MARKET and LIMIT orders
* CLI-based input
* Input validation
* Logging of requests and responses
* Clean modular structure

---

## 🚀 How to Run

### 1. Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 2. Run Commands

#### ▶️ Market Order

```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

#### ▶️ Limit Order

```bash
python cli.py BTCUSDT BUY LIMIT 0.001 60000
```

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── logs/
├── cli.py
├── requirements.txt
├── README.md
```

---

## 📝 Notes

Due to Binance demo/testnet API inconsistencies, order execution is simulated for reliability.
The architecture supports real API integration.

---

## 📄 Logs

Logs are stored in:

```
logs/trading.log
```

---

## ✅ Example Output

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
