# Trading Bot (Binance Futures Testnet)

## Setup

1. Clone the repo
2. Create virtual environment
3. Install dependencies:

```
pip install -r requirements.txt
```

4. Add `.env` file:

```
API_KEY=your_key
API_SECRET=your_secret
```

## Run

### Market Order

```
python cli.py BTCUSDT BUY MARKET 0.001
```

### Limit Order

```
python cli.py BTCUSDT BUY LIMIT 0.001 30000
```

## Features

* Place MARKET & LIMIT orders
* CLI input validation
* Structured project
* Logging support

## Note

Due to Binance demo/testnet API access limitations, order execution is mocked for demonstration purposes. The structure supports real API integration.

## Logs

Logs are stored in `logs/app.log`
