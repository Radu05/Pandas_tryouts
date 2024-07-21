'''
This is a test
'''

import	pandas as pd
import fnmatch

# pd.set_option('display.max_rows', 6000)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1920)

# base_partlist_1='partlist1.csv'

base_partlist_1='backup_changes1.csv'

changes_list_1='changes1.csv'

def import_partlist_csv(base_partlist):
	
	# Get the base_partlist from a csv file
	base_partlist_csv= pd.read_csv(base_partlist)
	
	# Make a back up of this file so that it will not be overwrittern 
	backup_partlist= base_partlist_csv.copy()
	
	# Clean the file by:
	
	# remove "RefDes" duplicates
	backup_partlist.drop_duplicates(subset=['Reference Designator'], keep='first', inplace=True, ignore_index=True)
	
	# remove useless components such as: HB*, KR*, P*, STP*, LP*, MH*
	remove_useless=['HB*', 'KR*', 'P*', 'STP*', 'LP*', 'MH*']

	for cases in remove_useless:

		print(cases)

		filtered = fnmatch.filter(backup_partlist['Reference Designator'], cases)

		for y in filtered:

			index_remove = backup_partlist.loc[backup_partlist['Reference Designator'] == y].index

			backup_partlist.drop(index= index_remove, inplace= True)		

	return(backup_partlist)

def import_changes_csv(changes_list):

	changes_list= pd.read_csv(changes_list)
	
	backup_changes= changes_list.copy()
	
	backup_changes.duplicated(subset= ['Reference Designator'])

backup_partlist = import_partlist_csv(base_partlist_1)

backup_partlist.to_csv('backup_partlist1.csv', index=False)

'''
print(df1.index)

value_to_find = 'sht1.cmp1280'

column_name = 'Component ID'

index = df1.loc[df1[column_name] == value_to_find].index

print(index)
'''
