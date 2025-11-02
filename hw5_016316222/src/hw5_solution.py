"""
HW5 Solution - All tasks 1-5
Student ID: 016316222
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('../data/accident_100k.csv')
df = df[df['State'].isin(['CA', 'FL', 'TX', 'NY'])]
df['Date'] = pd.to_datetime(df['Weather_Timestamp'], errors='coerce')
df = df.dropna(subset=['Date'])

# Task 1
daily_counts = df.groupby(['State', 'Date']).size().reset_index(name='Accident_Count')

plt.figure(figsize=(14, 6))
for state in ['CA', 'FL', 'TX', 'NY']:
    state_data = daily_counts[daily_counts['State'] == state]
    plt.plot(state_data['Date'], state_data['Accident_Count'], label=state)

plt.xlabel('Date')
plt.ylabel('Daily Accident Count')
plt.title('Daily Accident Counts by State (CA, FL, TX, NY)')
plt.legend(title='State')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../plots/task1_daily_accidents_by_state.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

# Task 2
df['DayOfWeek'] = df['Date'].dt.day_name()

normalized = df.groupby('State')['DayOfWeek'].value_counts(normalize=True).reset_index(name='Frequency')
pivot_data = normalized.pivot(index='DayOfWeek', columns='State', values='Frequency')

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_data = pivot_data.reindex(day_order)

plt.figure(figsize=(8, 6))
sns.heatmap(pivot_data, annot=True, fmt='.2f', cmap='YlOrRd', cbar_kws={'label': 'Proportion'})
plt.title('Accident Density by Day-of-Week and State')
plt.xlabel('State')
plt.ylabel('Day of Week')
plt.tight_layout()
plt.savefig('../plots/task2_heatmap_dayofweek_state.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

# Task 3
task3_df = df[df['Weather_Condition'].isin(['Fair', 'Mostly Cloudy', 'Cloudy', 'Clear'])]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
states = ['CA', 'FL', 'TX', 'NY']

for idx, state in enumerate(states):
    row = idx // 2
    col = idx % 2
    ax = axes[row, col]
    
    state_data = task3_df[task3_df['State'] == state]
    sns.boxplot(data=state_data, x='Weather_Condition', y='Severity', ax=ax)
    
    means = state_data.groupby('Weather_Condition')['Severity'].mean()
    x_positions = range(len(means))
    ax.scatter(x_positions, means.values, color='red', marker='D', s=100, 
               zorder=10, label='Mean' if idx == 0 else '')
    
    ax.set_title(f'Accident Severity in {state}')
    ax.set_xlabel('Weather Condition')
    ax.set_ylabel('Severity')
    if idx == 0:
        ax.legend()

plt.tight_layout()
plt.savefig('../plots/task3_severity_weather.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

# Task 4
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
states = ['CA', 'FL', 'TX', 'NY']

max_freq = 0
for state in states:
    state_data = df[df['State'] == state]['Severity']
    counts, _ = np.histogram(state_data, bins=4, range=(1, 4))
    max_freq = max(max_freq, counts.max())

for idx, state in enumerate(states):
    row = idx // 2
    col = idx % 2
    ax = axes[row, col]
    
    state_data = df[df['State'] == state]['Severity']
    ax.hist(state_data, bins=4, range=(1, 4), edgecolor='black', alpha=0.7)
    
    ax.set_title(f'Accident Severity Distribution in {state}')
    ax.set_xlabel('Severity')
    ax.set_ylabel('Frequency')
    ax.set_xlim(1, 4)
    ax.set_ylim(0, max_freq * 1.1)

plt.tight_layout()
plt.savefig('../plots/task4_severity_histogram.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()
# Task 5

