import pandas as pd

class Solution :
    def teamLeaders ( self , employee : pd.DataFrame ) -> pd.DataFrame :
        report_counts = employee.groupby('leaderId').size().reset_index(name='count')
        frequent_leaders = report_counts[report_counts['count'] >= 4]
        result = pd.merge(frequent_leaders, employee[['id', 'name']], left_on='leaderId', right_on='id')
        return result[['name']].drop_duplicates().reset_index(drop=True)