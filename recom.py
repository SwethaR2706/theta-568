import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')
file_path = "/content/Movie.csv"
df = pd.read_csv(file_path)
movies_df=pd.read_csv('/content/Movie.csv')
movies_df[0:5]
len(movies_df.userId.unique())
user_movies_df=movies_df.pivot(index='userId',columns='movie',values='rating').reset_index(drop=True)
user_movies_df
user_movies_df.index=movies_df.userId.unique()
user_movies_df.fillna(0,inplace=True)
user_movies_df
