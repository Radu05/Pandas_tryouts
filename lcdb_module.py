import pandas as pd
import os
import fnmatch

#Save curent working directory
start_path = os.getcwd()

#Get the lcdb path, converte it to table, remove unwanted entries, and save it to C:\zuken\000_PartlistManager
os.chdir(os.path.join(os.environ.get('CR8_LIB_ROOT'), 'searchdata'))

lcdb = pd.read_table('Packed_Part', sep='\x01', names= ['Partnumber', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Package', '11', '12', '13', '14', '15', 'Value', '16', 'Tolerance', '17', '18', '19', '20', '21', '22'])

lcdb.drop(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'], axis= 1, inplace= True)

remove_unwanted_PNs = ['A*', 'B*', 'C*', 'D*', 'E*', 'F*', 'G*', 'H*', 'I*', 'J*', 'K*', 'L*', 'M*', 'N*', 'O*', 'P*', 'Q*', 'R*', 'S*', 'T*', 'U*', 'V*', 'W*', 'X*', 'Y*', 'Z*']

for cases in remove_unwanted_PNs:
    filter1 = fnmatch.filter(lcdb['Partnumber'], cases)
    for x in filter1:
        lcdb.drop(index=lcdb.loc[lcdb['Partnumber'] == x].index, inplace= True)

try:
    os.mkdir('C:\\zuken\\_PartlistManager')
except FileExistsError:
    print("Directory already exists. Skipping...")

os.chdir('C:\\zuken\\_PartlistManager')

lcdb.to_csv('lcdb_clean.csv', index= False)