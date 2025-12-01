import logging
import os

def setup_logging():
    # Create logs folder
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log"),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger("sales_app")
    logger.debug("Logger initialized successfully")
    return logger