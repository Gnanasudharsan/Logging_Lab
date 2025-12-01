import logging

class SalesAnalyzer:
    def __init__(self):
        self.logger = logging.getLogger("sales_app.analyzer")

    def compute_average_weight(self, df):
        self.logger.info("Calculating average weight...")

        weight_col = df.columns[df.columns.str.contains("Weight", case=False)].tolist()
        if not weight_col:
            self.logger.error("No weight column found")
            raise KeyError("No column containing 'Weight'")
    
        col_name = weight_col[0]
        avg = df[col_name].mean()
        self.logger.debug(f"Average weight from column '{col_name}': {avg}")
        return avg

    def compute_max_height(self, df):
        self.logger.info("Calculating maximum height...")

        height_col = df.columns[df.columns.str.contains("Height", case=False)].tolist()
        if not height_col:
            self.logger.error("No height column found")
            raise KeyError("No column containing 'Height'")

        col_name = height_col[0]
        max_val = df[col_name].max()
        self.logger.debug(f"Maximum height from column '{col_name}': {max_val}")
        return max_val