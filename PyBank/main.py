# PyBank Task

# Import the libraries needed:

import os
import csv

# Read and open CSV file:

csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    # Remove colum headers:

    hearder_line = next(csvreader)
    
    # Initital statement:
            
    print("Financial Analysis")
    print("--------------------------------------------------")

    # Calculation of total months and total profit and loss:
    
    months = []
    profit_and_loss = []
    
    for row in csvreader:
        months.append(row[0])
        profit_and_loss.append(int(row[1]))
    
    total_months = len(months)
    print(f'Total Months: {total_months}')

    total_amount = sum(profit_and_loss)
    print(f'Total: ${total_amount}')

    # Calculation of average change of profit and loss:
    
    change = [0,]

    for i in range(len(profit_and_loss)-1):
       change.append(int(profit_and_loss[i + 1] - profit_and_loss[i]))
           
    average_change = sum(change) / (len(change)-1)
    print("Average Change: $" + "%.2f" % average_change)

    # Calculation of the greatest increase and greatest decrease in profits:

    greatest_increase = max(change)
    print(f'Greatest Increase in Profits: {months[int(change.index(greatest_increase))]} (${str(greatest_increase)})')

    greatest_decrease = min(change)
    print(f'Greatest Decrease in Profits: {months[int(change.index(greatest_decrease))]} (${str(greatest_decrease)})')
