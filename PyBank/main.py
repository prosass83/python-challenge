import os
import csv

# This will allow us to create file paths across operating systems

#budgetData = os.path.join('raw_data', 'budget_data_1.csv')
budgetData = os.path.join('raw_data', 'budget_data_2.csv')

#Initialiating variables
numberMonths = 0
totalRevenue = 0
initialRevenue = 0
lastMonthRevenue = 0
currentMonthRevenue = 0
revenueChange = 0
totalRevenueChange = 0
avgRevenueChange = 0
greatestRevenueIncrease = 0
greatestRevenueDecrease = 0

# Read in the CSV file
with open(budgetData, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the headers
    next(csvreader, None)  
    # Loop through the data
    
    for row in csvreader:
        numberMonths = numberMonths + 1
        currentMonthRevenue = int(row[1])
        #Finding the revenue of the first month
        if (initialRevenue == int(0)):
            initialRevenue = currentMonthRevenue
        totalRevenue = totalRevenue + currentMonthRevenue
        revenueChange = currentMonthRevenue - lastMonthRevenue
        totalRevenueChange = totalRevenueChange + revenueChange

        if (revenueChange > greatestRevenueIncrease):
            greatestRevenueIncrease = revenueChange
            monthWithGreatestIncrease = row[0]
        if (revenueChange < greatestRevenueDecrease):
            greatestRevenueDecrease = revenueChange
            monthWithGreatestDecrease = row[0]
        #Preparing for next month evaluation
        lastMonthRevenue = currentMonthRevenue
    finalRevenue = row[1]
    AvgRevenueChange = totalRevenueChange / numberMonths
    #Print results

    print("Total Months: " + str(numberMonths))
    print("Total Revenue: " + str(totalRevenue))
    print("Average Revenue Change: " + str(AvgRevenueChange))
    print("Greatest Increase in Revenue: " + str(monthWithGreatestIncrease) + " (" + str(greatestRevenueIncrease) + ") ")
    print("Greatest Decrease in Revenue: " + str(monthWithGreatestDecrease) + " (" + str(greatestRevenueDecrease) + ") ")
        
    #Write results to file
    # Specify the file to write to
    output_path = os.path.join('output', 'new.csv')

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Total Months', str(numberMonths)])
        csvwriter.writerow(['Total Revenue', str(totalRevenue)])
        csvwriter.writerow(['Average Revenue Change', str(AvgRevenueChange)])
        csvwriter.writerow(['Greatest Increase in Revenue', str(monthWithGreatestIncrease) , str(greatestRevenueIncrease)])
        csvwriter.writerow(['Greatest Increase in Revenue', str(monthWithGreatestDecrease) , str(greatestRevenueDecrease)])
    
