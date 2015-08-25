import pandas as pd
import matplotlib.pyplot as plt

gh_frame = pd.read_csv('gh_data.csv')


# .value_counts = 

# Anuj Adhiya                 1118
# Nichole Elizabeth DeMeré     546
# Morgan Brown                 411

# group by and get count 

user_counts = gh_frame['Who_Posted'].value_counts()

x_axis = range(len(user_counts))

plt.bar(x_axis, user_counts)
plt.show()

# The first step of this is to create a boolean series (just like a matrix is called a dataframe in pandas, a vector is called a series) that contains True for rows that we want to keep, and False for rows that we don't want to.

# screen_1 = progress_frame["screen"] == 1


# user_equals_46578 = progress_frame["user"] == 46578
# user_46578_frame = progress_frame[user_equals_46578]
# The above code will select only the rows of progress_frame where the user column equals 46578, and assigns the result to user_46578_frame.




