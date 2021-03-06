# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:12:34 2015

@author: reneehosogi
"""

# # Joining (Merging) DataFrames

# Using the [MovieLens 100k data](http://grouplens.org/datasets/movielens/), let's create two DataFrames:
# 
# - **movies**: shows information about movies, namely a unique **movie_id** and its **title**
# - **ratings**: shows the **rating** that a particular **user_id** gave to a particular **movie_id** at a particular **timestamp**

# ### Movies

import pandas as pd

file_path = '/Users/reneehosogi/Documents/GitHub_Clones/GA-SEA-DAT1/data/'
movie_url = file_path + 'u.item'
movie_cols = ['movie_id', 'title']
movies = pd.read_table(movie_url, sep='|', header=None, names=movie_cols, usecols=[0, 1])
movies.head()


# ### Ratings

rating_url = file_path + 'u.data'
rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(rating_url, sep='\t', header=None, names=rating_cols)
ratings.head()


# Let's pretend that you want to examine the ratings DataFrame, but you want to know the **title** of each movie rather than its **movie_id**. The best way to accomplish this objective is by "joining" (or "merging") the DataFrames using the Pandas `merge` function:

movie_ratings = pd.merge(movies, ratings)
movie_ratings.head()

# Here's what just happened:
# 
# - Pandas noticed that movies and ratings had one column in common, namely **movie_id**. This is the "key" on which the DataFrames will be joined.
# - The first **movie_id** in movies is 1. Thus, Pandas looked through every row in the ratings DataFrame, searching for a movie_id of 1. Every time it found such a row, it recorded the **user_id**, **rating**, and **timestamp** listed in that row. In this case, it found 452 matching rows.
# - The second **movie_id** in movies is 2. Again, Pandas did a search of ratings and found 131 matching rows.
# - This process was repeated for all of the remaining rows in movies.
# 
# At the end of the process, the movie_ratings DataFrame is created, which contains the two columns from movies (**movie_id** and **title**) and the three other colums from ratings (**user_id**, **rating**, and **timestamp**).
# 
# - **movie_id** 1 and its **title** are listed 452 times, next to the **user_id**, **rating**, and **timestamp** for each of the 452 matching ratings.
# - **movie_id** 2 and its **title** are listed 131 times, next to the **user_id**, **rating**, and **timestamp** for each of the 131 matching ratings.
# - And so on, for every movie in the dataset.

print(movies.shape)
print ratings.shape
print(movie_ratings.shape)


# Notice the shapes of the three DataFrames:
# 
# - There are 1682 rows in the movies DataFrame.
# - There are 100000 rows in the ratings DataFrame.
# - The `merge` function resulted in a movie_ratings DataFrame with 100000 rows, because every row from ratings matched a row from movies.
# - The movie_ratings DataFrame has 5 columns, namely the 2 columns from movies, plus the 4 columns from ratings, minus the 1 column in common.
# 
# By default, the `merge` function joins the DataFrames using all column names that are in common (**movie_id**, in this case). The [documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html) explains how you can override this behavior.

# ## Four Types of Joins

# There are actually four types of joins supported by the Pandas `merge` function. Here's how they are described by the documentation:
# 
# - **inner:** use intersection of keys from both frames (SQL: inner join)
# - **outer:** use union of keys from both frames (SQL: full outer join)
# - **left:** use only keys from left frame (SQL: left outer join)
# - **right:** use only keys from right frame (SQL: right outer join)
# 
# The default is the "inner join", which was used when creating the movie_ratings DataFrame.
# 
# It's easiest to understand the different types by looking at some simple examples:

# ### Example DataFrames A and B

A = pd.DataFrame({'color': ['green', 'yellow', 'red'], 'num':[1, 2, 3]})
A


B = pd.DataFrame({'color': ['green', 'yellow', 'pink'], 'size':['S', 'M', 'L']})
B


# ### Inner join
# 
# Only include observations found in both A and B:

pd.merge(A, B, how='inner')


# ### Outer join
# 
# Include observations found in either A or B:

pd.merge(A, B, how='outer')


# ### Left join
# 
# Include all observations found in A:

pd.merge(A, B, how='left')


# ### Right join
# 
# Include all observations found in B:

pd.merge(A, B, how='right')



### Excercise 1: Seattle Pronto Cycle Share data merge
"""
Using the Pronto Cycle Share year one data for https://www.prontocycleshare.com/datachallenge
We want to merge the dockcount values from 2015_station_data.csv into 2015_trip_data.csv.
In particular we want the dockcount column from 2015_station_data.csv to be added to the rows in 2015_trip_data.csv.
# to create a single dataframe called trip_and_station_data.
"""

## import pandas as pd
import pandas as pd

# read in the data from '2015_trip_data.csv' file into a dataframe names 'file_path' and examine the contents.
# name the file trip_data

file_path = '/Users/reneehosogi/Documents/GA-SEA-DAT1-master/data/pronto_cycle_share/'
trip_data_url = file_path + '2015_trip_data.csv'
trip_data = pd.read_table(trip_data_url, sep=',', header=0)
trip_data.head()
trip_data.shape


# read in the data from just columns name and dockcount from 2015_trip_data.csv  file and examine the contents
station_data_url= '/Users/reneehosogi/Documents/GA-SEA-DAT1-master/data/pronto_cycle_share/2015_trip_data.csv'
station_data = pd.read_table(rating_url, sep='\t', header=None, names=rating_cols)
rating_cols = ['trip_id','starttime','stoptime','bikeid','tripduration','from_station_name','to_station_name,from_station_id','to_station_id','usertype','gender', 'birthyear']


"""
Merge trip_data with station_data, joining on trip_data 'station_name' and station_data 'name.
Since we do not know if there is a 'name' in station_data that matches each station_name in trip_data do a left merge
Name the resulting dataframe trip_and_dockcount_data.
"""

trip_and_dockcount_data = pd.merge(trip_data, station_data, how='left', left_on='from_station_name', right_on='station_data')



# Your code here


# Remove the 'name' column

# Your code here


# Bonus: check to see if there are any rows that have no value in the dockcount columns.

# Your code here