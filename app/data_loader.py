import pandas as pd
import logging

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = logging.getLogger("sales_app.data_loader")

    def load(self):
        self.logger.info(f"Loading dataset from {self.file_path}")

        try:
            df = pd.read_csv(self.file_path)
            self.logger.debug(f"Dataset shape: {df.shape}")
            return df

        except FileNotFoundError:
            self.logger.exception("Could not find the dataset file")
            raise

        except Exception:
            self.logger.exception("Unexpected error while loading data")
            raise