import pandas as pd

class Solution:
    def frequent_commenters(self, df: pd.DataFrame) -> pd.DataFrame:
        # Step 1: Filter where the author commented on their own article
        self_comments = df[df['author_id'] == df['viewer_id']]

        # Step 2: Count the frequency of comments for each author
        comment_counts = self_comments['author_id'].value_counts()

        # Step 3: Filter authors who have commented more than once (> 1)
        frequent_authors = comment_counts[comment_counts > 1].index

        # Step 4: Create the result DataFrame, rename the column, and sort in ascending order
        result_df = pd.DataFrame({'id': frequent_authors})
        result_df = result_df.sort_values(by='id', ascending=True).reset_index(drop=True)

        return result_df