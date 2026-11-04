import pandas as pd

class Solution:
    def secondHighestSalary(self, employee: pd.DataFrame) -> pd.DataFrame:
        unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
        if len(unique_salaries) >= 2:
            second_highest = unique_salaries.iloc[1]
            return pd.DataFrame({'SecondHighestSalary': [second_highest]})
        else:
            return pd.DataFrame({'SecondHighestSalary': [None]})