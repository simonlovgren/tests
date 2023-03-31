```
================================================================================
Create initial DataFrames DF1 and DF2
================================================================================

Here we simply set up two DataFrames, DF1 and DF2, of which DF1 will be our
source dataset and DF2 will be the filter we want to apply to DF1 in order
to get a DataFrame containing only relevant rows we want to see/work on.

------------------
|      DF1       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  0 |   1 |   6 |
|  1 |   2 |   7 |
|  2 |   3 |   8 |
|  3 |   4 |   9 |
|  4 |   5 |   0 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------
|   DF2    |
------------
|    |   A |
|---:|----:|
|  0 |   2 |
|  1 |   4 |
------------
<class 'pandas.core.frame.DataFrame'>



================================================================================
Create filtered View/Slice using DF2 as filter for DF1.
================================================================================

This creates a"copy of a slice from a DataFrame" from DF1 which will
cause issues when we want to add columns, or modify, the "new" filtered
DataFrame later.

code: sdf = df1.iloc[1:3,]

------------------
|      SDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  2 |   3 |   8 |
------------------
<class 'pandas.core.frame.DataFrame'>



================================================================================
Create filtered DataFrame using DF2 as filter for DF1.
================================================================================

This creates a"copy of a slice from a DataFrame" from DF1 which will
cause issues when we want to add columns, or modify, the "new" filtered
DataFrame later.

code: fdf = df1[df1['A'].isin(df2['A'])]

------------------
|      FDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>



================================================================================
Create explicit copy of filtered DataFrame
================================================================================

This creates an explicit copy of the filtered DataFrame, which no longer has any
link to the original DataFrame. Therefore it should not generate the
"SettingWithCopy" warning if modified.

code: fdfc = fdf.copy()

------------------
|      FDFC      |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>



================================================================================
Modify values in column B of DF1
================================================================================

Note how the value is propagated to the View/slice SDF we created, but not to
any of the other "filtered" DataFrames/slices/copies.

code: df1.loc[:,'B'] = df1['B'] * 10

------------------
|      DF1       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  0 |   1 |  60 |
|  1 |   2 |  70 |
|  2 |   3 |  80 |
|  3 |   4 |  90 |
|  4 |   5 |   0 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      FDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      SDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |  70 |
|  2 |   3 |  80 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      FDFC      |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>



================================================================================
Modify values in column B of DF1
================================================================================

Note how, using the nested syntax, the values are changed in df1, but is not
reflected in the View/slice nor the other "filtered" DataFrames/slices/copies.
By doing this we've broken the link between DF1 and SDF.

code: df1['B'] = df1['B'] * 10

------------------
|      DF1       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  0 |   1 | 600 |
|  1 |   2 | 700 |
|  2 |   3 | 800 |
|  3 |   4 | 900 |
|  4 |   5 |   0 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      FDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      SDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |  70 |
|  2 |   3 |  80 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      FDFC      |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>



================================================================================
Add new column C to DF1
================================================================================

Now we add a new column C to DF1. This, too, is a modification which is not
reflected in any view, slice or copy.

code: df1['C'] = df1['A'] * 2

------------------------
|         DF1          |
------------------------
|    |   A |   B |   C |
|---:|----:|----:|----:|
|  0 |   1 | 600 |   2 |
|  1 |   2 | 700 |   4 |
|  2 |   3 | 800 |   6 |
|  3 |   4 | 900 |   8 |
|  4 |   5 |   0 |  10 |
------------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      FDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      SDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |  70 |
|  2 |   3 |  80 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      FDFC      |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>



================================================================================
Add D to filtered DataFrame FDF
================================================================================

Now we try to add a new column D to the filtered DataFrame, since we only want
to work on this subset of data. However, since FDF is a "Copy of a slice" we'll
get the "SettingWithCopyWarning".

code: fdf['D'] = fdf['A'] * 3

dataframe_slices.py:161: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead
System.Management.Automation.RemoteException
See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  fdf['D'] = fdf['A'] * 3

------------------------
|         DF1          |
------------------------
|    |   A |   B |   C |
|---:|----:|----:|----:|
|  0 |   1 | 600 |   2 |
|  1 |   2 | 700 |   4 |
|  2 |   3 | 800 |   6 |
|  3 |   4 | 900 |   8 |
|  4 |   5 |   0 |  10 |
------------------------
<class 'pandas.core.frame.DataFrame'>

------------------------
|         FDF          |
------------------------
|    |   A |   B |   D |
|---:|----:|----:|----:|
|  1 |   2 |   7 |   6 |
|  3 |   4 |   9 |  12 |
------------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      SDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |  70 |
|  2 |   3 |  80 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      FDFC      |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |   7 |
|  3 |   4 |   9 |
------------------
<class 'pandas.core.frame.DataFrame'>



================================================================================
Add E to explicit copy of filtered DataFrame (FDFC)
================================================================================

Now we add a new column to the explicit copy of the filtered DataFrame. Since
it is an explicit copy, with no link to the original DataFrame, we will not
get the "SettingWithCopyWarning" when performing this operation.

code: fdfc['E'] = fdfc['A'] * 4

------------------------
|         DF1          |
------------------------
|    |   A |   B |   C |
|---:|----:|----:|----:|
|  0 |   1 | 600 |   2 |
|  1 |   2 | 700 |   4 |
|  2 |   3 | 800 |   6 |
|  3 |   4 | 900 |   8 |
|  4 |   5 |   0 |  10 |
------------------------
<class 'pandas.core.frame.DataFrame'>

------------------------
|         FDF          |
------------------------
|    |   A |   B |   D |
|---:|----:|----:|----:|
|  1 |   2 |   7 |   6 |
|  3 |   4 |   9 |  12 |
------------------------
<class 'pandas.core.frame.DataFrame'>

------------------
|      SDF       |
------------------
|    |   A |   B |
|---:|----:|----:|
|  1 |   2 |  70 |
|  2 |   3 |  80 |
------------------
<class 'pandas.core.frame.DataFrame'>

------------------------
|         FDFC         |
------------------------
|    |   A |   B |   E |
|---:|----:|----:|----:|
|  1 |   2 |   7 |   8 |
|  3 |   4 |   9 |  16 |
------------------------
<class 'pandas.core.frame.DataFrame'>
```
