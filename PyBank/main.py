# PyBank Task

# Import the libraries needed:

import os
import csv

# Initital statement:
            
header = "Financial Analysis"
print(header)

separator = "--------------------------------------------------"
print (separator)

# Read and open CSV file:

csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    # Headers:

    hearder_line = next(csvreader)
    
    # Calculation of total months and total profit and loss:
    
    months = []
    profit_and_loss = []
    
    for row in csvreader:
        months.append(row[0])
        profit_and_loss.append(int(row[1]))
    
    total_months = f'Total Months: {len(months)}'
    print(total_months)
    total_amount = f'Total: ${sum(profit_and_loss)}'
    print(total_amount)

    # Calculation of average change of profit and loss:
    
    change = [0,]

    for i in range(len(profit_and_loss)-1):
       change.append(int(profit_and_loss[i + 1] - profit_and_loss[i]))
           
    change_formula = sum(change) / (len(change)-1)
    average_change = "Average Change: $" + "%.2f" % change_formula
    print(average_change)

    # Calculation of the greatest increase and greatest decrease in profits:

    greatest_increase = f'Greatest Increase in Profits: {months[int(change.index(max(change)))]} (${str(max(change))})'
    print(greatest_increase)
    greatest_decrease = f'Greatest Decrease in Profits: {months[int(change.index(min(change)))]} (${str(min(change))})'
    print(greatest_decrease)

# Export results to "Analysis" text file:

output_path = os.path.join("Analysis","Analysis.txt")
with open (output_path,"w") as output_file:
    output_file.write(str(header) + '\n')
    output_file.write(str(separator) + '\n')
    output_file.write(str(total_months) + '\n')
    output_file.write(str(total_amount) + '\n')
    output_file.write(str(average_change) + '\n')
    output_file.write(str(greatest_increase) + '\n')
    output_file.write(str(greatest_decrease) + '\n')