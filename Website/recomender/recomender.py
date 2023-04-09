# Nesessary libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

# Load Data into data frame 
# Data Source: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
books = pd.read_csv('Website/recomender/Books.csv')
ratings = pd.read_csv('Website/recomender/Ratings.csv')
users = pd.read_csv('Website/recomender/Users.csv')

books = books.dropna() 

ratings_name = ratings.merge(books ,on='ISBN') # merge ratings and books data set 

# filter users who gave more reviews to books 
a = ratings_name.groupby('User-ID').count()['Book-Title']>300 # 
geninue_users = a[a].index
geniune_user = ratings_name[ratings_name['User-ID'].isin(geninue_users)]

# filter books who got more then 50 ratings 
b = geniune_user.groupby('Book-Title').count()['Book-Rating']>=50
famous_books = b[b].index
final_df = geniune_user[geniune_user['Book-Title'].isin(famous_books)]

final_df.drop_duplicates()
# only allow the columns that can be aggregated.
final_df = final_df.drop(["ISBN", "Book-Author", "Publisher","Image-URL-S", "Image-URL-M", "Image-URL-L"], axis='columns')

# reference: https://www.kaggle.com/code/jagdishchavan/book-recommender-system
pivot_table = final_df.pivot_table(index='Book-Title',columns='User-ID', aggfunc='first')
pivot_table.fillna(0,inplace=True)

# caluclate eucledian distance for given data
cos_simscore = cosine_similarity(pivot_table)

# function to recomend books 
def recommend(books_name):
    index = np.where(pivot_table.index==books_name)[0][0]    
    similar_books = sorted(list(enumerate(cos_simscore[index])),key=lambda x:x[1],reverse=True)[1:6]
    books = []
    for i in similar_books:
        books.append(pivot_table.index[i[0]])
    return books


print(recommend('The Fellowship of the Ring (The Lord of the Rings, Part 1)'))
