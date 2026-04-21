import logging
import os

# Create logs folder if not exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)