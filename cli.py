import sys
from bot.orders import place_order
import bot.logging_config  # initialize logging


def main():
    args = sys.argv[1:]

    if len(args) < 4:
        print("\nUsage:")
        print("MARKET: python cli.py BTCUSDT BUY MARKET 0.001")
        print("LIMIT : python cli.py BTCUSDT BUY LIMIT 0.001 60000\n")
        return

    symbol = args[0]
    side = args[1]
    order_type = args[2]
    quantity = float(args[3])

    price = None
    if order_type.upper() == "LIMIT":
        if len(args) < 5:
            print("❌ Price required for LIMIT order")
            return
        price = float(args[4])

    print("\n===== ORDER REQUEST =====")
    print(f"Symbol   : {symbol}")
    print(f"Side     : {side}")
    print(f"Type     : {order_type}")
    print(f"Quantity : {quantity}")

    if price:
        print(f"Price    : {price}")

    result = place_order(symbol, side, order_type.upper(), quantity, price)

    print("\n===== RESPONSE =====")
    for key, value in result.items():
        print(f"{key}: {value}")

    if "error" in result:
        print("\nResult: Failed ❌")
    else:
        print("\nResult: Success ✅")


if __name__ == "__main__":
    main()