import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from db import setup_db, load_movies
from db import MovieModel

session = setup_db()
movies = session.query(MovieModel).all()

df = pd.DataFrame([{'genre': r.genre, 'rating': r.rating} for r in movies])

rating_dist = df['rating'].value_counts().sort_index()
rating_dist.to_csv('rating_dist.csv', header=['count'])


plt.figure()
sns.histplot(data=df, x ='rating')
plt.title('Movie Ratings Distribution')
plt.tight_layout()
plt.savefig('rating_hist.png')

