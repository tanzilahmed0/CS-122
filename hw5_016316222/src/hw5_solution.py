"""
HW5: Tanzil Ahmed 
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('../data/accident_100k.csv')
states = ['CA', 'FL', 'TX', 'NY']
df = df[df['State'].isin(states)]
df['Date'] = pd.to_datetime(df['Weather_Timestamp'])
df = df.dropna(subset=['Date'])

# Task 1
daily_counts = df.groupby(['State', 'Date']).size().reset_index(name='Accident_Count')

plt.figure(figsize=(14, 6))
for state in states:
    state_data = daily_counts[daily_counts['State'] == state]
    plt.plot(state_data['Date'], state_data['Accident_Count'], label=state)

plt.xlabel('Date')
plt.ylabel('Daily Accident Count')
plt.title('Daily Accident Counts by State (CA, FL, TX, NY)')
plt.legend(title='State')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../plots/task1_timeseries.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()
'''
 Peak periods: Late 2019 from around August to Sep shows highest peaks, especially CA reaching ~60 daily accidents, 
 while Florida and Texas show moderate peaks (10-15) and NY remains consistently low (<5). 
 Temporal patterns: CA had extreme spikes in 2019, FL/TX show similar moderate patterns, 
 and NY is consistently low hroughout.
'''


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
plt.savefig('../plots/task2_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

'''
# Weekday/weekend contrast: CA, NY, and TX show the strongest contrast with weekday proportions being
# much higher than weekends. 
# Unusual patterns: CA's Monday is notably lower than mid-week peak.
'''
# Task 3
task3_df = df[df['Weather_Condition'].isin(['Fair', 'Mostly Cloudy', 'Cloudy', 'Clear'])]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

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
plt.savefig('../plots/task3_weather.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

'''
Florida stands out with the highest average accident severity, around 2.75 under Fair weather. It also 
shows the widest variation in severity, especially for Fair and Mostly Cloudy conditions. In contrast, 
California shows a much flatter distribution.
'''

# Task 4
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

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
plt.savefig('../plots/task4_histograms.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

'''
California, Florida, and New York are skewed toward minor accidents (Severity 2.0). Texas, on the other hand,
has a bimodal distribution, accidents are split between Severity 2.0 and 3.0. Across all states, there’s 
a strong spike at Severity 2.0 and a notable gap at Severity 2.5. Texas 
is unique for its second spike at 3.0.
'''

# Task 5
# Question: Does lower visibility lead to higher accident severity?
task5_df = df[['Visibility(mi)', 'Severity']].dropna()

plt.figure(figsize=(10, 6))
plt.scatter(task5_df['Visibility(mi)'], task5_df['Severity'], alpha=0.3, s=10)
plt.xlabel('Visibility (miles)')
plt.ylabel('Severity')
plt.title('Task 5: Does Lower Visibility Lead to Higher Accident Severity?')
plt.grid(True, alpha=0.3)

z = np.polyfit(task5_df['Visibility(mi)'], task5_df['Severity'], 1)
p = np.poly1d(z)
plt.plot(task5_df['Visibility(mi)'].sort_values(), p(task5_df['Visibility(mi)'].sort_values()), 
         "r--", linewidth=2, label='Trend Line')

plt.legend()
plt.tight_layout()
plt.savefig('../plots/task5_exploration.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

# Analysis: The scatter plot shows a very weak inverse relationship between visibility and accident severity, 
#

