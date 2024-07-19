import	pandas as pd
import  fnmatch

changes1 = pd.read_csv('changes1.csv')

backup_changes1 = changes1.copy()

backup_changes1.drop_duplicates(subset= ['Reference Designator'], keep= 'first', inplace= True, ignore_index= True)

print(backup_changes1)

filtered = fnmatch.filter(backup_changes1['Reference Designator'], 'T*')

print(filtered)

for x in filtered:

    index_remove = backup_changes1.loc[backup_changes1['Reference Designator'] == x].index

    print(index_remove)

    backup_changes1.drop(index= index_remove, inplace= True)

backup_changes1.to_csv('backup_changes1.csv')