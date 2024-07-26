import pandas as pd
import os
import fnmatch

start_path= os.getcwd()

print(start_path)

lcdb= os.environ.get('CR8_LIB_ROOT')

print(lcdb)

new_path= os.path.join(lcdb, 'searchdata')

os.chdir(new_path)

print(os.getcwd())

table= pd.read_table('Packed_Part', sep='\x01', names= ['Partnumber', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Package', '11', '12', '13', '14', '15', 'Value', '16', 'Tolerance', '17', '18', '19', '20', '21', '22'])

table.drop(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'], axis= 1, inplace= True)

remove_useless_PNs= ['A*', 'B*', 'C*', 'D*', 'E*', 'F*', 'G*', 'H*', 'I*', 'J*', 'K*', 'L*', 'M*', 'N*', 'O*', 'P*', 'Q*', 'R*', 'S*', 'T*', 'U*', 'V*', 'W*', 'X*', 'Y*', 'Z*']

for cases in remove_useless_PNs:
    
        filtered= fnmatch.filter(table['Partnumber'], cases)

        for x in filtered:

            index_remove= table.loc[table['Partnumber'] == x].index

            table.drop(index= index_remove, inplace= True)

os.chdir(start_path)

print(os.getcwd())

table.to_csv('lcdb_clean.csv', index= False)

print('Done')