# The Data we need to retrieve.
# 1. The totale number of votes cost.
# 2. A complete list of cadidates who received votes.
# 3. The percentage of votes each cadidate won. 
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote. 
#Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')
#with open(file_to_load) as election_data
#print(election_data)
import csv
import os
file_to_load = 'Resources/election_results.csv'
with open(file_to_load) as election_data:
    print(election_data)

#Assign a variable for the file to load and the path. 
#file_to_save = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #file_reader = csv.reader(election_data)  
   # headers = next(file_reader)

   # with open(file_to_save, “w”) as txt_file:

   # print(headers)  
    # print(election_data)
###Print the file object
