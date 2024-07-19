import fnmatch

lst = ['this','is','just','a','test']
filtered = fnmatch.filter(lst, 't*')

print(filtered)