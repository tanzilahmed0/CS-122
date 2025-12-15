import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

from database import init_db, get_all_books 

df = pd.read_csv('books.csv') 

df = df[['title', 'genre', 'rating']] 

genre_avg = df.groupby('genre')['rating'].mean().reset_index()
genre_avg.to_csv('genre_ratings.csv', index=False)

top5 = genre_avg.sort_values(ascending=False).head(5).reset_index()

plt.figure()
sns.barplot(data=top5, x='genre', y='rating')
plt.title('Top 5 Genres by Average Rating')
plt.tightlayout()
plt.savefig('genre_plot.png')
