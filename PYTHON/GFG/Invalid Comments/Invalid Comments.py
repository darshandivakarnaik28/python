import pandas as pd

def find_invalid_comments(df: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where the length of the 'content' column is greater than 20
    invalid_df = df[df['content'].str.len() > 20]

    # Return only the 'comment_id' column as a DataFrame
    return invalid_df[['comment_id']]