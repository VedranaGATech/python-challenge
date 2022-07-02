# Analyze the financial records of the company.
# Task is to create a Python script that analyzes the records to calculate each of the following values:
# 1- The total number of months included in the dataset
# 2- The net total amount of "Profit/Losses" over the entire period
# 3- The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4- The greatest increase in profits (date and amount) over the entire period
# 5- The greatest decrease in profits (date and amount) over the entire period
# 6- Final script should both print the analysis to the terminal, and export a text file with the results.

#import modules
import os
import csv

#define file path 
budget_data = os.path.join("Resources", "budget_data.csv")

#define variables/list  
total_months= []
profits_losses = []
monthly_change= []

total_profits = 0

#open the csv file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row first 
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}") - check to see if we need to 

        #loop through the rows of data after the header
    for row in csvreader:
        #append the Dates for total_months and and Profit/Losses for profits_losses information to their lists
        total_months.append(row[0])
        profits_losses.append(row[1])

        #calculate total_profit
        total_profits = total_profits + int(row[1])

 #loop through Profits/Losses to get the monthly_change
    for i in range(1, len(profits_losses)):
        #take the difference between the months and append to monthly_change
        monthly_change.append(int(profits_losses[i]) - int(profits_losses[i-1]))

#capture the max and min of the monthly_change list
max_increase_profit = max(monthly_change)
max_decrease_profit = min(monthly_change)

#use month list to index the max and min to the correct month by + 1 since the month correlated to change is the next month
max_increase_month = monthly_change.index(max(monthly_change)) + 1
max_decrese_month = monthly_change.index(min(monthly_change)) + 1 

#print Statements
print('Financial Analysis\n')
print('----------------------------\n')
print(f'Total Months: {len(total_months)}\n')
print(f'Total: ${total_profits}\n')
print(f'Average Change: {round(sum(monthly_change) / len(monthly_change), 2)}\n')
print(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_profit))})\n')
print(f'Greatest Decrease in Profits: {total_months[max_decrese_month]} (${(str(max_decrease_profit))})\n')

#define path for the Output file
budget_analysis_txt = os.path.join('analysis', 'budget_analysis.txt')

#export print to .txt file
with open(budget_analysis_txt, 'w') as text:
    text.write('Financial Analysis' + '\n')
    text.write('----------------------------' + '\n')
    text.write(f'Total Months: {len(total_months)}' + '\n')
    text.write(f'Total: ${total_profits}' + '\n')
    text.write(f'Average Change: {round(sum(monthly_change) / len(monthly_change), 2)}' + '\n')
    text.write(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_profit))})' + '\n')
    text.write(f'Greatest Decrease in Profits: {total_months[max_decrese_month]} (${(str(max_decrease_profit))})' + '\n')