# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:29:21 2024

@author: Gerald
"""

import pandas as pd

# Save url
url_file = "https://raw.githubusercontent.com/nedgerald/repo01/main/movie_dataset.csv"

# Accessing and reading movie dataset file
df_dataset  = pd.read_csv(url_file, index_col=False)

# Printing content of the movie dataset
print(url_file)


# Question 1 ###########################################################
   
# Find highest rating
hri = df_dataset['Rating'].idxmax()

# Get highest rated movie
hrm = df_dataset.loc[hri]

print("\nHighest rated movie: ", hrm)

#Question 2 ############################################################
    
# Average revenue of all movies
aram = df_dataset['Revenue (Millions)'].mean()

print("\nAverage revenue of all movies: ", aram)


# Question 3 ##############################################################

# Movies released between 2015 and 2017
movie_2015_2017 = df_dataset[(df_dataset['Year'] >= 2015) & (df_dataset['Year'] <= 2017)]

# Average revenue of movies released between 2015 and 2017
avg_rev = movie_2015_2017['Revenue (Millions)'].mean()

print("\nAverage revenue of movies from 2015 to 2017:", avg_rev)


# Question 4 #################################################################

# Data Frame for movies released in the year 2016
movies2016 = df_dataset[df_dataset['Year'] == 2016]

# Count the number of movies released in 2016
nbr_movies2016 = movies2016.shape[0]

print("\nNumber of movies released in 2016:", nbr_movies2016)

# Question 5: ################################################################

# Data Frame for movies directed by Christopher Nolan
cn_movies = df_dataset[df_dataset['Director'] == 'Christopher Nolan']

# Movies directed by Christopher Nolan
nbr_cn_movies = cn_movies.shape[0]

print("\nNumber of movies directed by Christopher Nolan:", nbr_cn_movies)


# Question 6 #################################################################

# Data Frame for movies with a rating of at least 8
hrm = df_dataset[df_dataset['Rating'] >= 8]

# Movies with a rating of at least 8
nbr_hrm = hrm.shape[0]

print("\nNumber of movies with a rating of at least 8:", nbr_hrm)  


# Question 7 #################################################################

# Christopher Nolan movies
cn_movies = df_dataset[df_dataset['Director'] == 'Christopher Nolan']

# Median rating of Christopher Nolan's movies
median_rating_movies = cn_movies['Rating'].median()

print("\nMedian rating of movies directed by Christopher Nolan:", median_rating_movies)


# Question 8 ##################################################################


avg_rating_year = df_dataset.groupby('Year')['Rating'].mean()

# Year with higest avg rate and Highest average rating
year_highest_average_rating = avg_rating_year.idxmax()
highest_average_rating = avg_rating_year.max()

print("\nYear with the highest average rating:", year_highest_average_rating)
print("Highest average rating:", highest_average_rating)

# Question 9 ##################################################################

#Data Frame for the years between 2006 and 2016
df_filtered = df_dataset[(df_dataset['Year'] >= 2006) & (df_dataset['Year'] <= 2016)]

# Count the number of movies for each year
mpy = df_filtered['Year'].value_counts().sort_index()

# Calculate the percentage increase from 2006 to 2016
movies_2006 = mpy[2006]
movies_2016 = mpy[2016]
per_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print("\nPercentage increase in the number of movies from 2006 to 2016:", round(per_increase, 2), "%")

# Question 10 #################################################################
   
# Occurrences of each actor
cnt_ac = df_dataset['Actors'].value_counts()

# Get the most common actor
cm_actor = cnt_ac.idxmax()
nbr_movies_cm_actor = cnt_ac.max()

print("\nMost common actor:", cm_actor)
print("Number of movies:", nbr_movies_cm_actor)

# Question 11 ##################################################################


genres = df_dataset['Genre'].str.split(',')

# Create a list to store all unique genres
all_genres = []

# Iterate over the lists of genres in each row
for genre_list in genres:
    # Extend the all_genres list with the unique genres in the current row
    all_genres.extend(genre_list)

# Use a set to get unique genres
unique_genres = set(all_genres)

# Print the count of unique genres and the list of unique genres
print("\nCount of Unique Genres:", len(unique_genres))
print("Unique Genres:", unique_genres)

# Question 12 ##################################################################
   
# Numerical columns for correlation analysis
df_correlation = df_dataset.select_dtypes(include=['int64', 'float64'])

# Correlation matrix
matrix = df_correlation.corr()

# Print the correlation matrix
print("\nCorrelation Matrix: ", matrix)

# What insights can you deduce? Mention at least 5 insights.
print("\nInsights deduce")
print("1 - There is a strong positive correlation of approximately 0.64 between the number of votes a movie receives and its revenue")
print("2 - There is a strong positive correlation of about 0.63 between the Metascore (a score based on reviews from critics) and the user rating")
print("3 - There is a negative correlation of approximately -0.41 between the release year of a movie and the number of votes it receives.")
print("4 - The correlation between the Metascore and the revenue of a movie is relatively weak (about 0.14). ")
print("5 - The correlation between the runtime of a movie and its rating is moderate (about 0.39).")

# And what advice can you give directors to produce better movies?
print("\nAdvice given to directors to produce better movies")
print("To produce better movies, directors should prioritize compelling storytelling, understand their audience, collaborate effectively, focus on character development, and strive for technical excellence while staying true to their artistic vision.")

# Question 13 ###################################################################################
   
# Save the cleaned data to a new CSV file
url_file.to_csv("cleaned_movie_dataset.csv", index=False)

# Output the URL link to the Python file
username = "nedgerald"
repository_name = "repo01"
file_name = "css4p01.py"
url = ""
print("URL link to the Python file:", url)