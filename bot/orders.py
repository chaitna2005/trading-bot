from bot.client import get_client

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        # 🔥 MOCK RESPONSE (simulate Binance success)
        return {
            "orderId": 123456789,
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED",
            "executedQty": quantity,
            "avgPrice": price if price else "75000"
        }

    except Exception as e:
        return {"error": str(e)}