#import os and csv
import os
import csv

#join the path for the csv
budget_data = os.path.join('Resources', 'budget_data.csv')

#lists for data
months = []
profit = []
profit_change = []

#create variables 
total_profit = 0

#opens the csv file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        #add data from first row 
        months.append(row[0])

        #add data from second row into total_profit
        profit.append(int(row[1]))
        #calculate the total profit 
        total_profit = total_profit + int(row[1])

    #read rows in the profits/losses 
    #used Source 1 here to find the profit change rows 33-44
    for x in range(1, len(profit)):
        profit_change.append((int(profit[x]) - int(profit[x-1])))
    
    # calculate average of the profit change
        profit_average = sum(profit_change) / len(profit_change)

        #calculate the greatest and leastest increase of profits 
        max_profits = max(profit_change)
        min_profits = min(profit_change)

        max_month = months[profit_change.index(max_profits)+1]
        min_month = months[profit_change.index(min_profits)+1]
      

#print results
print('Financial Analysis')
print("-------------------------")
print('Total Months:  ' + str(len(months)))
print('Total Profits: $' + str(total_profit))
print('Average Change: $' + str(round(profit_average, 2)))
print('Greatest Increase in Profits: ' + str(max_month) + ' ($' + str(max_profits) + ')')
print('Greatest Decrease in Profits: ' + str(min_month) + ' ($' + str(min_profits)+ ')')

# Specify the file to write to
output_path = os.path.join("PyBank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the text
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(['Total Months:  ' + str(len(months))])
    csvwriter.writerow(['Average Change: $' + str(round(profit_average, 2))])
    csvwriter.writerow(['Greatest Increase in Profits: ' + str(max_month) + ' ($' + str(max_profits) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits: ' + str(min_month) + ' ($' + str(min_profits)+ ')'])