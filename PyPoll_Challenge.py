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
#file_to_load = 'Election_Analysis/Resources/election_results.csv'
file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0 
total_ct_votes = 0
#Declare new list candidate options
candidate_options = []
#Declare an empty dicitonary
candidate_votes = {}

#1 : Create a county list and county votes dictionary
county = []
county_votes = {}

#Declaring Winning candidate and winning count tracker
winning_candidate = ""
winning_county = ""
winning_count = 0
winning_percentage = 0

#2. Track the largest county and county voter turnout.
with open(file_to_load) as election_data:
    #print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    #print(headers)
    for row in file_reader:
    #    print(row)
        total_ct_votes += 1

        county_name = row[1]
        #print(county)
        if county_name not in county:
        #Add it to the list
            county.append(county_name)
    #print(county)
        #2. Begin tracking that candidate's vote count.
            county_votes[county_name] = 0
        #print(county_votes)
    # Add a vote to that candidate's count
        county_votes[county_name] += 1
    #print(county_votes)
#Open the election results and read the file. 

with open(file_to_load) as election_data:
   # print(election_data)
        #Read the file object with the reader function
    file_reader = csv.reader(election_data)
        #Print each row in the CSV file
        #Print the header row.
    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
            #print(row)
        #2. Add to the total vote count.
        total_votes += 1

         #Print the candidate name from each row
        candidate_name = row[2]


        #3. Extract the county name from each row



        #Add the candidate name to the candidate list 3.5.2
        #candidate_options.append(candidate_name)

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        #Add it to the list
            candidate_options.append(candidate_name)

        #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
    # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #Save the results to our text file. 
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal. 
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the txt file. 
    txt_file.write(election_results)
    
    for county_name in county_votes:
        #print(county_name)
        ct_votes = county_votes.get(county_name)
        ct_vote_percentage = float(ct_votes) / float(total_ct_votes) *100
        county_results = (
            f"{county_name}: {ct_vote_percentage:.1f}% ({ct_votes:,})\n")

        print(county_results)
        txt_file.write(county_results)
    


    if (ct_votes > winning_count) and (ct_vote_percentage > winning_percentage):
        winning_count = ct_votes
        winning_county = county_name
        winning_percentage = ct_vote_percentage
        
          

        winning_county_summary = (
            f"\n"
            f"------------------------\n"
            f"Largest County Turnout: Denver\n"
            f"------------------------\n\n")
        print(winning_county_summary)
        txt_file.write(winning_county_summary)
        #3. Print the total votes.
        #print(total_votes)
        #Print the candidate list.
        #print(candidate_options)
        #print(candidate_votes)
    #Determine the percentage of votes for each candidate by looping through the counts.
    #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. retrieve vote count of a candidate. 
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)
        #4. Print the candidate name and percentage of votes. 
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
            #To do  print out each candidate's name, vote count, and percentage of votes to the terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count and percentage to the terminal.
        
        #Save the candidate results to our next text file
    



        #Determine winning vote count and candidate
        #1. Determine if teh votes are greater than the winning count 3.5.5. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. Set the winning_candidate equal to the candidate's name. 
            winning_candidate = candidate_name
            # TO DO  print out the winning candidate, vote count and percentage to the terminal
        #Selft attempt print(winning_candidate, " is the winning candidate with", winning_count, "votes, equal to ", winning_percentage, "%")
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n")
    print(winning_candidate_summary)
        #Save the winning candidate's name to the text file. 
    txt_file.write(winning_candidate_summary)
