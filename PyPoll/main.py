# PyPoll Task

# Import the libraries needed:

import os
import csv

# Initital statement:
            
header = "Election Results"
print(header)

separator = "--------------------------------------------------"
print (separator)

# Identify location of the output file:

output_path = os.path.join("Analysis","Analysis.txt")

# Identify location, read and open CSV file:

csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath,"r") as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=",")

    # Headers:

    hearder_line = next(csvreader)

    # Identify Variables:

    total_votes = 0
    candidates = []
    candidate_votes = {}
    winner = "x"
    winner_votes = 0

    # Read through te file and identify total number of votes and list of candidates who received votes:

    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidates:
           candidates.append(candidate_name)
           candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

    total_votes_result = f'Total Votes: {total_votes}'

# Open the output file to start printing and exporting the results:

with open (output_path,"w") as output_file:
    
    print(total_votes_result)
    print(separator)
    output_file.write(str(header) + '\n')
    output_file.write(str(separator) + '\n')
    output_file.write(str(total_votes_result) + '\n')
    output_file.write(str(separator) + '\n')

    # Calculate percetage of votes and total number of votes per candidate:
     
    for candidates in candidate_votes:
        votes = candidate_votes[candidates]
        percentage = votes / total_votes * 100
        results = f'{candidates}: {percentage: .3f}% ({votes})'
        
        print(results)
        output_file.write(str(results) + '\n')

    # Identify the winner:

        if votes > winner_votes:
            winner_votes = votes
            winner = candidates
        
    print (separator)
    output_file.write(str(separator) + '\n')

    winner_name = f'Winner: {winner}'
    
    print (winner_name)
    print (separator)
    output_file.write(str(winner_name) + '\n')
    output_file.write(str(separator) + '\n')