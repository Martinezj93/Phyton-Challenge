# PyPoll Task

# Import the libraries needed:

import os
import csv

# Read and open CSV file:

csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

# Remove headers:

    hearder_line = next(csvreader)
    
    # Initital statement:
            
    print("Election Results")
    print("--------------------------------------------------")

    # Calculation of total months and total profit and loss:
    
    votes = []
        
    for row in csvreader:
        votes.append(row[0])
    
    total_votes = len(votes)
    print(f'Total Months: {votes}')