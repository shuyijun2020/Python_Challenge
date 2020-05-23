import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Total month
    Totmonth = 0
    Totsum = 0
    change = 0
    Totchange = 0
    Greatestincrease = 0
    Greatestdecrease = 99999999
    
    # Read each row of data after the header
    for row in csvreader:
    # Total number of months       
        Totmonth = Totmonth + 1
    # Total months (Totmonth) and  total sum (Totsum) of profit/losses, change in profit/losses, 
    # Total change (Totchange), previous row value (prerow)
        Totsum = Totsum + int(row[1])
        if Totmonth > 1:
            change = int(row[1]) - prerow
            Totchange = Totchange + change
        prerow = int(row[1])

        if change > Greatestincrease:
            Greatestincrease = change
        if change < Greatestdecrease:
            Greatestdecrease = change
    
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months:", Totmonth)
    print("Total:", Totsum)
    print("Average Change:", Totchange / (Totmonth-1))
    print("Greatest Increase in Profits:", "($",Greatestincrease, ")")
    print("Greatest Decrease in Profits:", "($",Greatestdecrease, ")")

    with open("Budget_Analysis.text", 'w') as text:
        text.write('Financial Analysis \n')
        text.write('-------------------------------  \n')
        text.write(f'Total Months: {Totmonth} \n')
        text.write(f'Average Change: {"{:.2f}".format(Totchange / (Totmonth-1))} \n')
        text.write(f'Greatest Increase in Profits: ($ {Greatestincrease} ) \n')
        text.write(f'Greatest Decrease in Profits: ($ {Greatestdecrease} ) \n')















    # print("Number of months")
    # Num_Months = len(open(csvpath).readlines()) - 1
    # print(Num_Months)







 