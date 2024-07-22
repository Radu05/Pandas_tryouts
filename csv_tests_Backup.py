'''
This is a test
'''

import	pandas as pd
import fnmatch

# pd.set_option('display.max_rows', 6000)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1920)

base_partlist_name= 'partlist1.csv'

changes_list_name= 'changes1.csv'

def get_sheetframe_info(partlist):

	# Drop all rowns that are not containg sheetframe info

	# remove_useless(partlist)

	index_sheetframe= partlist.loc[partlist['Symbol Name'] == 'din_a1_v_sdsym_2.smb'].index

	sheetframe_info1= partlist.take(index_sheetframe, axis= 0)

	sheetframe_symbols=fnmatch.filter(partlist['Symbol Name'], 'din_a1_v_sdsym_1.smb')

	for shtfrm in sheetframe_symbols:

		index_concat= partlist.loc[partlist['Symbol Name'] == shtfrm].index

		sheetframe_info2= partlist.take(index_concat, axis= 0)

	sheetframe_info1= pd.concat([sheetframe_info1, sheetframe_info2])

	return(sheetframe_info1)

def import_partlist_csv(base_partlist):
		
	# Make a back up of this file so that it will not be overwrittern 
	backup_partlist= base_partlist.copy()
	
	# Clean the file by:
	
	# remove "RefDes" duplicates
	backup_partlist.drop_duplicates(subset= ['Reference Designator'], keep= 'first', inplace= True, ignore_index= True)
		
	return(backup_partlist)

def remove_useless_nets(partlist):

	# Remove Net related components (sheetconnectors /gnds /voltage rails)
	remove_useless_nets= ['shcon*.smb','nc.smb','gndd*.smb','volt*.smb','export*.smb']

	for cases in remove_useless_nets:

		filtered= fnmatch.filter(partlist['Symbol Name'], cases)

		for x in filtered:
		
			index_remove= partlist.loc[partlist['Symbol Name'] == x].index

			partlist.drop(index= index_remove, inplace= True)
	
	return(partlist)

def remove_useless_comp(partlist):

	# remove useless components such as: HB*, KR*, P*, STP*, LP*, MH*
	remove_useless_comp= ['HB*', 'KR*', 'P*', 'STP*', 'LP*', 'MH*']

	for cases in remove_useless_comp:

		print(cases)

		filtered = fnmatch.filter(partlist['Reference Designator'], cases)

		for y in filtered:

			index_remove= partlist.loc[partlist['Reference Designator'] == y].index

			partlist.drop(index= index_remove, inplace= True)

	return(partlist)
	
# Get the base_partlist from a csv file
base_partlist_input= pd.read_csv(base_partlist_name)

# print(base_partlist_input)

# Get the sheetframe symbol information
sheetframe_info_input= get_sheetframe_info(base_partlist_input)

sheetframe_info_input.to_csv('sheetframe_info_input.csv', index=False)

print('Done')
'''
backup_partlist_input= import_partlist_csv(base_partlist_input)

backup_partlist_input.to_csv('backup_partlist_input.csv', index=False)
'''