class Solution:

    def employeeProjects(self, employee_projects):
        # Group by 'employee_id' and count distinct 'project_id' values
        df = (
            employee_projects.groupby('employee_id')['project_id']
            .nunique()
            .reset_index(name='cnt')
        )

        return df