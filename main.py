from app.logger_config import setup_logging
from app.data_loader import DataLoader
from app.analyzer import SalesAnalyzer

def main():
    logger = setup_logging()
    logger.info("Application started")

    loader = DataLoader("data/sales_data.csv")
    df = loader.load()

    analyzer = SalesAnalyzer()

    avg_weight = analyzer.compute_average_weight(df)
    logger.info(f"Average Weight: {avg_weight}")

    max_height = analyzer.compute_max_height(df)
    logger.info(f"Maximum Height: {max_height}")

    logger.info("Application finished successfully")

if __name__ == "__main__":
    main()