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
    changeloc1 = ""
    changeloc2 = ""
    Totchange = 0
    Averagechange = 0
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
            Averagechange = Totchange / (Totmonth-1)
        prerow = int(row[1])

        if change > Greatestincrease:
            Greatestincrease = change
            changeloc1 = row[0]
      
        if change < Greatestdecrease:
            Greatestdecrease = change
            changeloc2 = row[0]
    
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months:", Totmonth)
    print("Total:", Totsum)
    print("Average Change:", round(Averagechange, 2))
    print("Greatest Increase in Profits:", changeloc1, "($",Greatestincrease, ")")
    print("Greatest Decrease in Profits:", changeloc2, "($",Greatestdecrease, ")")

    with open("Budget_Analysis.text", 'w') as text:
        text.write('Financial Analysis \n')
        text.write('-------------------------------  \n')
        text.write(f'Total Months: {Totmonth} \n')
        text.write(f'Average Change: {"{:.2f}".format(Averagechange)} \n')
        text.write(f'Greatest Increase in Profits: {changeloc1}, ($ {Greatestincrease} ) \n')
        text.write(f'Greatest Decrease in Profits: {changeloc2}, ($ {Greatestdecrease} ) \n')















    # print("Number of months")
    # Num_Months = len(open(csvpath).readlines()) - 1
    # print(Num_Months)







 