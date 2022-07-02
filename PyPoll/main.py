 #Task is to create a Python script that analyzes the votes and calculates each of the following values:
    # 1- The total number of votes cast
    # 2- A complete list of candidates who received votes
    # 3- The percentage of votes each candidate won
    # 4- The total number of votes each candidate won
    # 5- The winner of the election based on popular vote
    # 6- Final script should both print the analysis to the terminal, and export a text file with the results


#import modules 
import os
import csv

#define file path 
election_data_csv = os.path.join('Resources', 'election_data.csv')

#define variables/list
candidate = []
vote_count = []
vote_percent = []

total_votes = 0

#open csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header
    csv_header = next(csvreader)

    #loop through the rows
    for row in csvreader:

        #find total vote count
        total_votes += 1

        #add candidate name and a vote to the list
        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            vote_count.append(1)

        #if the candidate is already on the list, add a vote count to them
        else:
            index = candidate.index(row[2])
            vote_count[index] += 1

    #add to vote_percent list 
    for votes in vote_count:
        #define percentage total formula
        percentage = (votes / total_votes)
        #append vote_percent list 
        vote_percent.append(percentage)

    #find the winning candidate by max vote count
    winner = max(vote_count)
    index = vote_count.index(winner)
    winning_candidate = candidate[index]

#print results 
print('Election Results\n')
print('--------------------------\n')
print(f'Total Votes: {str(total_votes)}\n')
print('--------------------------\n')
for i in range(len(candidate)):
    print(f'{candidate[i]}: {(vote_percent[i]):.3%} ({str(vote_count[i])})\n')
print('--------------------------\n')
print(f'Winner: {winning_candidate}\n')
print('--------------------------')

#define output file path 
election_analysis = os.path.join('analysis', 'election_analysis.txt')

#export to .txt file
with open(election_analysis, 'w') as text:
    text.write('Election Results' + '\n')
    text.write('--------------------------' + '\n')
    text.write(f'Total Votes: {str(total_votes)}' + '\n')
    text.write('--------------------------' + '\n')
    for i in range(len(candidate)):
        text.write(f'{candidate[i]}: {(vote_percent[i]):.3%} ({str(vote_count[i])})' + '\n')
    text.write('--------------------------' + '\n')
    text.write(f'Winner: {winning_candidate}' + '\n')
    text.write('--------------------------' + '\n')