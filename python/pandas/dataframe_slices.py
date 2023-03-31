import pandas as pd


def print_df(df, name):
    md = df.to_markdown()
    tlen = max(len(md.splitlines()[0]), len(name))
    print('-' * tlen)
    print(f'|{name:^{tlen-2}}|')
    print('-' * tlen)
    print(md)
    print('-' * tlen)
    print(type(df))
    print()

def title(name):
    print('\n')
    print('=' * max(len(name), 80))
    print(name)
    print('=' * max(len(name), 80))
    print()


def paragraph(text):
    lines = [l.strip() for l in text.splitlines()]

    # Drop empty first- and last line(s)
    if not lines[0]:
        lines = lines[1:]
    if not lines[-1]:
        lines = lines[:-1]

    # Print all remaining lines
    print('\n'.join(lines))
    print()





# -------------------------------------------------------------

title('Create initial DataFrames DF1 and DF2')
paragraph('''
Here we simply set up two DataFrames, DF1 and DF2, of which DF1 will be our
source dataset and DF2 will be the filter we want to apply to DF1 in order
to get a DataFrame containing only relevant rows we want to see/work on.
''')

df1 = pd.DataFrame({
    'A' : [1,2,3,4,5],
    'B' : [6,7,8,9,0]
})

df2 = pd.DataFrame({
    'A' : [2,4]
})

print_df(df1, 'DF1')
print_df(df2, 'DF2')

# -------------------------------------------------------------

title('Create filtered View/Slice using DF2 as filter for DF1.')
paragraph('''
This creates a"copy of a slice from a DataFrame" from DF1 which will
cause issues when we want to add columns, or modify, the "new" filtered
DataFrame later.

code: sdf = df1.iloc[1:3,]
''')

sdf = df1.iloc[1:3,]
print_df(sdf, 'SDF')

# -------------------------------------------------------------

title('Create filtered DataFrame using DF2 as filter for DF1.')
paragraph('''
This creates a"copy of a slice from a DataFrame" from DF1 which will
cause issues when we want to add columns, or modify, the "new" filtered
DataFrame later.

code: fdf = df1[df1['A'].isin(df2['A'])]
''')

fdf = df1[df1['A'].isin(df2['A'])]
print_df(fdf, 'FDF')

# -------------------------------------------------------------

title('Create explicit copy of filtered DataFrame')
paragraph('''
This creates an explicit copy of the filtered DataFrame, which no longer has any
link to the original DataFrame. Therefore it should not generate the
"SettingWithCopy" warning if modified.

code: fdfc = fdf.copy()
''')

fdfc = fdf.copy()
print_df(fdfc, 'FDFC')

# -------------------------------------------------------------

title('Modify values in column B of DF1')
paragraph('''
Note how the value is propagated to the View/slice SDF we created, but not to
any of the other "filtered" DataFrames/slices/copies.

code: df1.loc[:,'B'] = df1['B'] * 10
''')
df1.loc[:,'B'] = df1['B'] * 10
print_df(df1, 'DF1')
print_df(fdf, 'FDF')
print_df(sdf, 'SDF')
print_df(fdfc, 'FDFC')

# -------------------------------------------------------------

title('Modify values in column B of DF1')
paragraph('''
Note how, using the nested syntax, the values are changed in df1, but is not
reflected in the View/slice nor the other "filtered" DataFrames/slices/copies.
By doing this we've broken the link between DF1 and SDF.

code: df1['B'] = df1['B'] * 10
''')
df1['B'] = df1['B'] * 10
print_df(df1, 'DF1')
print_df(fdf, 'FDF')
print_df(sdf, 'SDF')
print_df(fdfc, 'FDFC')


# -------------------------------------------------------------

title('Add new column C to DF1')
paragraph('''
Now we add a new column C to DF1. This, too, is a modification which is not
reflected in any view, slice or copy.

code: df1['C'] = df1['A'] * 2
''')
df1['C'] = df1['A'] * 2
print_df(df1, 'DF1')
print_df(fdf, 'FDF')
print_df(sdf, 'SDF')
print_df(fdfc, 'FDFC')


# -------------------------------------------------------------

title('Add D to filtered DataFrame FDF')
paragraph('''
Now we try to add a new column D to the filtered DataFrame, since we only want
to work on this subset of data. However, since FDF is a "Copy of a slice" we'll
get the "SettingWithCopyWarning".

code: fdf['D'] = fdf['A'] * 3
''')
fdf['D'] = fdf['A'] * 3
print_df(df1, 'DF1')
print_df(fdf, 'FDF')
print_df(sdf, 'SDF')
print_df(fdfc, 'FDFC')


# -------------------------------------------------------------

title('Add E to explicit copy of filtered DataFrame (FDFC)')
paragraph('''
Now we add a new column to the explicit copy of the filtered DataFrame. Since
it is an explicit copy, with no link to the original DataFrame, we will not
get the "SettingWithCopyWarning" when performing this operation.

code: fdfc['E'] = fdfc['A'] * 4
''')
fdfc['E'] = fdfc['A'] * 4
print_df(df1, 'DF1')
print_df(fdf, 'FDF')
print_df(sdf, 'SDF')
print_df(fdfc, 'FDFC')