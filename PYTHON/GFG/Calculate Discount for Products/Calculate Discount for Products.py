import pandas as pd

class Solution:
    def calculateDiscount(self, products: pd.DataFrame) -> pd.DataFrame:
        condition = (products['product_id'] % 2 == 0) & (products['category'].str.startswith('A'))
        products['discount'] = products['price'].where(condition, 0)
        result = products[['product_id', 'discount']].sort_values(by='product_id', ascending=True)
        return result