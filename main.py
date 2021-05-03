import json
import csv
from urllib.request import urlopen


url = 'https://raw.githubusercontent.com/champ1432/RBL/master/ZGMH_League_2_2021_regular_season_29-14.json'

# Opening JSON file and loading the data
# into the variable data
json_url = urlopen(url)
export = json.loads(json_url.read())
  
teamdata = export['teams']
  
# now we will open a file for writing
data_file = open('data_file.csv', 'w')
  
# create the csv writer object
csv_writer = csv.writer(data_file)
  
# Counter variable used for writing 
# headers to the CSV file
count = 0
  
for team in teamdata:
    if count == 0:
  
        # Writing headers of CSV file
        header = team.keys()
        csv_writer.writerow(header)
        count += 1
  
    # Writing data of CSV file
    csv_writer.writerow(team.values())
  
data_file.close()
print('done')