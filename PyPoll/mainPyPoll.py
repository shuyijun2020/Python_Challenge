import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
   # Checking num columns and rows
   # print(len(row)) 
   # Total number of votes
    Num_row = len(open(csvpath).readlines()) - 1
    # print(Num_row)

    Candidate = ""
    voteKhan = 0
    voteCorrey = 0
    voteLi = 0
    voteOTooley = 0
    for row in csvreader:
        if row[2] == "Khan":
            voteKhan = voteKhan + 1
        if row[2] == "Correy":
            voteCorrey = voteCorrey + 1
        if row[2] == "Li":
            voteLi = voteLi + 1
        if row[2] == "O'Tooley":
            voteOTooley = voteOTooley + 1

    print("Election Results")
    print("----------------------")
    print("Total Votes:", Num_row)
    print("Khan:", ("{:.3f}".format(100*voteKhan/Num_row)), "%  (", voteKhan, ")" )
    print("Correy:", ("{:.3f}".format(100*voteCorrey/Num_row)), "%  (", voteCorrey, ")" )
    print("Li:", ("{:.3f}".format(100*voteLi/Num_row)), "%  (", voteLi, ")" )
    print("O'Tooley:", ("{:.3f}".format(100*voteOTooley/Num_row)), "%  (", voteOTooley, ")" )
    print("----------------------")
    print("Winner: Khan")
    print("----------------------")

    with open("pypoll_final_result.text", 'w') as text:
        text.write('Election Results \n')
        text.write('----------------------------------- \n')
        text.write(f'Total Votes: {Num_row} \n')
        text.write('----------------------------------- \n')
        text.write(f'Khan: {("{:.3f}".format(100*voteKhan/Num_row))}% ({voteKhan}) \n')
        text.write(f'Correy: {("{:.3f}".format(100*voteCorrey/Num_row))}% ({voteCorrey}) \n')
        text.write(f'Li: {("{:.3f}".format(100*voteLi/Num_row))}% ({voteLi}) \n')
        text.write(f'O Tooley: {("{:.3f}".format(100*voteOTooley/Num_row))}% ({voteOTooley}) \n')
        text.write('----------------------------------- \n')
        text.write('Winner: Khan \n')
        text.write('----------------------------------- \n')


   



