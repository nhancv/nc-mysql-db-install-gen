# 2017 Apr 17
# --Nhan Cao--
# 
import os
import json
import fileinput
from pprint import pprint

with open('install.conf.json') as data_file:    
	data = json.load(data_file)

##########################################################
for line in fileinput.input("./install.sql", inplace=True): 
	print line.rstrip().replace('DB_NAME', data['DB_NAME'])

for line in fileinput.input("./install.sql", inplace=True): 
	print line.rstrip().replace('DB_USER', data['DB_USER'])

for line in fileinput.input("./install.sql", inplace=True): 
	print line.rstrip().replace('DB_PASSWORD', data['DB_PASSWORD'])

for line in fileinput.input("./install.sql", inplace=True): 
	print line.rstrip().replace('DB_HOST', data['DB_HOST'])

print("Finish Generate")
os.system("mysql -u root -p < install.sql")
print("Finish Install")




