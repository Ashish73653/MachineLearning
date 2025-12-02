import pandas as pd
from pathlib import Path

# Load the IPL dataset
df = pd.read_csv("data/most_runs_average_strikerate.csv")   # update the path if needed
print(df.head())

# Display basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Display summary statistics of the dataset
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values in the dataset
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Fill missing values with mean for average column
df['average'] = df['average'].fillna(df['average'].mean())
print("\nData after filling missing values in 'average' column:")
print(df.head())
print(df.isnull().sum())

# Filter players with average greater than 40
high_average_player = df[df['average'] > 40]
print("\nPlayers with Average greater than 40:")
print(high_average_player)

# Filter players with strike rate greater than 170
high_strike_rate_player = df[df['strikerate'] > 170]
print("\nPlayers with Strike Rate greater than 170:")
print(high_strike_rate_player)

# Find the top 5 players with the highest runs
top_scorers = df.nlargest(5, 'total_runs')
print("\nTop 5 Players with Highest Runs:")
print(top_scorers)

# Sort players by average in descending order
# Skip players with average less than 10, then sort by average descending
filtered = df[df['average'] >= 10]
sorted_by_average = filtered.sort_values(by='average', ascending=True)
print("\nPlayers with Average >= 10 sorted by Average in descending order:")
print(sorted_by_average)

# Save the cleaned dataset to a new CSV file next to this script
output_path = Path(__file__).resolve().parent / "cleaned_ipl_data.csv"
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset saved to {output_path}")
