import pandas as pd

def find_salesperson_without_blue_orders(df_salesperson: pd.DataFrame, df_orders: pd.DataFrame, df_company: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Find the com_id of the company named 'BLUE'
    blue_com_id = df_company.loc[df_company['name'] == 'BLUE', 'com_id']

    # Step 2: Find all sales_id that have placed orders with the company 'BLUE'
    sales_with_blue = df_orders[df_orders['com_id'].isin(blue_com_id)]['sales_id'].unique()

    # Step 3: Filter salespersons whose sales_id is NOT in the list of salespersons who ordered from 'BLUE'
    result = df_salesperson[~df_salesperson['sales_id'].isin(sales_with_blue)][['name']]

    return result