#import os and csv
import os
import csv

#join the path for the csv
election_data = os.path.join('..', 'Resources', 'election_data.csv')

#list of data
votes = []
candidates = []
candidates_list = []

#opens the csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        #add data from the rows needed
        votes.append(row[0])
        candidates_list.append(row[2])
    
    #was working on this part last but could never figure out
    for candidates in candidates_list:
        if candidates not in candidates_list:
            candidates_list = sum(candidates)


#print results
print('Election Results')
print("-------------------------")
print('Total Votes:  ' + str(len(votes)))
print("-------------------------")
print(candidates)


# Specify the file to write to
output_path = os.path.join("PyPoll.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the text
    csvwriter.writerow([('Election Results')])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(['Total Votes:  ' + str(len(votes))])
    csvwriter.writerow(["-------------------------"])


