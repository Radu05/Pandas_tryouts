'''
This is a test
'''

import	pandas as pd
from fnmatch import filter


# pd.set_option('display.max_rows', 6000)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1920)

base_partlist_1 = 'partlist1.csv'

changes_list_1 = 'changes1.csv'

def import_partlist_csv( base_partlist ):
	
	# Get the base_partlist from a csv file
	base_partlist_csv = pd.read_csv( base_partlist )
	
	# Make a back up of this file so that it will not be overwrittern 
	backup_partlist = base_partlist_csv.copy()
	
	# Clean the file by:
	
	# remove "RefDes" duplicates
	backup_partlist.drop_duplicates( subset = ['Reference Designator'], keep = 'first', inplace = True, ignore_index = True )
	
	# remove useless components such as: HB*, KR*, P*, STP*, LP*, MH*
	
	# ser = pd.Series(backup_partlist['Reference Designator'])

	# print(ser.dtypes)

	# print(ser.str.match('HB'))

	print(backup_partlist['Reference Designator'].dtypes)

	backup_partlist.convert_dtypes(convert_string=True)

	print(backup_partlist['Reference Designator'].dtypes)

	# index_HB = backup_partlist.loc[ filter( backup_partlist['Reference Designator'].converst_dtypes(convert_string=True), 'HB5000' ) ].index

	# print(index_HB)

	# remove_HB1 = backup_partlist.drop( index = index_HB , axis = 0 )

	# print( remove_HB1 )

	# remove_HB1.to_csv( 'remove_HB1.csv', index = False )


def import_changes_csv( changes_list ):

	changes_list = pd.read_csv( changes_list )
	
	backup_changes = changes_list.copy()
	
	backup_changes.duplicated( subset = ['Reference Designator'] )

import_partlist_csv( base_partlist_1 )

'''
print(df1.index)

value_to_find = 'sht1.cmp1280'

column_name = 'Component ID'

index = df1.loc[df1[column_name] == value_to_find].index

print(index)
'''
