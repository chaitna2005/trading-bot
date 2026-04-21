import logging
import random
from bot.validators import validate_order

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        # Validate input
        validate_order(symbol, side, order_type, quantity, price)

        logging.info(f"Order Request: {symbol} {side} {order_type} {quantity} {price}")

        # Simulated response (stable + interview-safe)
        if order_type == "MARKET":
            response = {
                "orderId": random.randint(100000, 999999),
                "symbol": symbol,
                "status": "FILLED",
                "type": "MARKET",
                "side": side,
                "executedQty": quantity,
                "avgPrice": "65000.50"
            }

        elif order_type == "LIMIT":
            response = {
                "orderId": random.randint(100000, 999999),
                "symbol": symbol,
                "status": "NEW",
                "type": "LIMIT",
                "side": side,
                "price": price,
                "origQty": quantity
            }

        logging.info(f"Order Response: {response}")
        return response

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {"error": str(e)}