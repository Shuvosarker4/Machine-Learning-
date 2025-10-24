import pandas as pd


df = pd.read_csv('student_data.csv')


# select and filter

# all name of a specific column
print(df['FullName']) # FullName is a column of the data file
# multiple column
print(df[['FullName','Location']])
print(df.loc[0]) # all info of 0 index student
print(df['Algorithm Marks']>50) # return True False
# df['Age'] = 20 add a new column
# df['Age'] = df['Age'] + 1 Modify column
# df.drop('City', axis = 1, inplace = True) Delete Column

print(df.head()) # First 5 rows
print(df.head(2)) # First 2 rows
print(df.tail()) # Last 5 rows
print(df.tail(3)) # Last 3 rows

df.columns # Get all column ['ID', .. .. ..]
df.index # Get index from 0 to ..

print(df.info()) # summary of the DF output below 
"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 9 columns):
 #   Column                Non-Null Count  Dtype
---  ------                --------------  -----
 0   StudentID             20 non-null     object
 1   FullName              20 non-null     object
 2   Data Structure Marks  16 non-null     float64
 3   Algorithm Marks       16 non-null     float64
 4   Python Marks          15 non-null     float64
 5   CompletionStatus      20 non-null     object
 6   EnrollmentDate        20 non-null     object
 7   Instructor            20 non-null     object
 8   Location              20 non-null     object
dtypes: float64(3), object(6)
memory usage: 1.5+ KB
"""

print(df.sample()) # random row all info
print(df.describe()) # gives statistical summary for numeric column
"""
Data Structure Marks  Algorithm Marks  Python Marks
count             16.000000        16.000000     15.000000    
mean              84.000000        84.000000     85.666667    
std                6.501282         6.501282      5.394000    
min               72.000000        72.000000     76.000000    
25%               79.500000        79.500000     83.000000    
50%               85.500000        85.500000     85.000000    
75%               88.250000        88.250000     88.500000    
max               94.000000        94.000000     95.000000
"""