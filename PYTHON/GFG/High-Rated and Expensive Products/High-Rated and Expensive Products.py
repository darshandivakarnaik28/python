import pandas as pd

class Solution:
    def filterHighRatedExpensive(self, df: pd.DataFrame) -> pd.DataFrame:
        # Filter products based on rating, stock availability, and price
        filtered_df = df[
            (df['rating'] >= 4.5) & 
            (df['quantity_in_stock'] > 0) & 
            (df['price'] >= 300)
        ]
        return filtered_df