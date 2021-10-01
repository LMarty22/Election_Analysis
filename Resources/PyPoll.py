# The Data we need to retrieve.
# 1. The totale number of votes cost.
# 2. A complete list of cadidates who received votes.
# 3. The percentage of votes each cadidate won. 
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote. 
#Assign a variable for the file to load and the path.

#import csv
#import os
#file_to_load = 'Election_Analysis/Resources/election_results.csv'
#with open(file_to_load) as election_data:
 #   file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the opne() funciton with the "w" mode we will write data to the file.
 #   open(file_to_save, "w")
#Create a filename variable to a direct or indirect path to the file. 
  #  file_to_save = os.path.join("analysis", "election_analysis.txt")

#using the with statement open the file as a text file.
 #   outfile = open(file_to_save, "w")
    #Write some data to the file. 
 #   outfile.write("Hello World")
    #Close the file
 #   outfile.close()

#Create a filename variable to a direct or indirect path to the file. 
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the with statement open the file as a text file. 
#with open(file_to_save, "w") as txt_file:
    #Write some data to the file. 
#  txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")

#Add out dependencies
import csv 
import os 
#Assign a variable to load a file from a path. 
file_to_load = 'Election_Analysis/Resources/election_results.csv'
#Assign a variable to save the file to a path
file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt")

#Open the election results and read the file. 
with open(file_to_load) as election_data:
    print(election_data)
        #Read the file object with the reader function
    file_reader = csv.reader(election_data)
        #Print each row in the CSV file
    for row in file_reader:
            print(row)