import pandas as pd

class Solution:
    def countCityPopulationCategories(self, cities: pd.DataFrame) -> pd.DataFrame:
        # Define categories based on population criteria
        def get_category(pop):
            if pop < 100000:
                return 'Small City'
            elif 100000 <= pop <= 1000000:
                return 'Medium City'
            else:
                return 'Large City'

        # Assign a category to each city
        cities['category'] = cities['population'].apply(get_category)

        # Define all required categories to ensure they always appear even if counts are 0
        all_categories = ['Small City', 'Medium City', 'Large City']

        # Group by category and count the number of city IDs
        counts = cities.groupby('category')['city_id'].count().reset_index()
        counts.rename(columns={'city_id': 'cities_count'}, inplace=True)

        # Merge with all categories to ensure missing categories show 0
        result_df = pd.DataFrame({'category': all_categories})
        result_df = result_df.merge(counts, on='category', how='left').fillna(0)

        # Convert cities_count to integer
        result_df['cities_count'] = result_df['cities_count'].astype(int)

        return result_df