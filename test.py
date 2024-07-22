import fnmatch

lst = ['this','is','just','a','test']
filtered = fnmatch.filter(lst, 't*')

print(filtered)

'''
print(df1.index)

value_to_find = 'sht1.cmp1280'

column_name = 'Component ID'

index = df1.loc[df1[column_name] == value_to_find].index

print(index)
'''