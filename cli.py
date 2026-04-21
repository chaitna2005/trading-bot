import typer
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

app = typer.Typer()

setup_logging()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    try:
        validate_input(symbol, side, order_type, quantity, price)

        print("\nOrder Request:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        result = place_order(symbol, side, order_type, quantity, price)

        print("\nResponse:")
        print(result)

        if "error" in result:
            print("\nResult: Failed ❌")
        else:
            print("\nResult: Success ✅")

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    app()