import pandas as pd

def mode_of_scores(df: pd.DataFrame) -> pd.DataFrame:
    # Count the frequency of each score
    counts = df['score'].value_counts()

    # Find the maximum frequency
    max_freq = counts.max()

    # Filter scores that have the maximum frequency
    mode_scores = counts[counts == max_freq].index

    # Create the result dataframe with 'score' and 'mode' columns, ordered by score ascending
    result = pd.DataFrame({
        'score': sorted(mode_scores),
        'mode': max_freq
    })

    return result