import	pandas as pd
import  fnmatch

# changes1 = pd.read_csv('changes1.csv')

changes1 = pd.read_csv('partlist1.csv')

backup_changes1 = changes1.copy()

print(backup_changes1)

# remove useless components such as: HB*, KR*, P*, STP*, LP*, MH*
# remove_useless=['HB*', 'KR*', 'P*', 'STP*', 'LP*', 'MH*']
remove_useless=['shcon*.smb','nc.smb','gndd*.smb','volt*.smb','export*.smb']
for cases in remove_useless:

    filtered = fnmatch.filter(backup_changes1['Symbol Name'], cases)

    print(filtered)

    for x in filtered:

        index_remove = backup_changes1.loc[backup_changes1['Symbol Name'] == x].index

        print(index_remove)

        backup_changes1.drop(index= index_remove, inplace= True)

backup_changes1.drop_duplicates(subset= ['Reference Designator'], keep= 'first', inplace= True, ignore_index=True)

backup_changes1.to_csv('backup_changes1.csv')
