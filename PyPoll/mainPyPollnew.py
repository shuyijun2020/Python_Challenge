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

    countvote = []
    totalvote = 0
    unique = []
    percent = []
    candidatecount = []
    
    

    for row in csvreader:
        # candidate name row[2]
        totalvote = totalvote + 1

        if row[2] not in unique:
            unique.append(row[2])
        countvote.append(row[2])

    for candidate in unique:
        
        candidatecount.append(countvote.count(candidate))
        percent.append(round(countvote.count(candidate)/totalvote*100,3))
        
        winner = unique[candidatecount.index(max(candidatecount))]

    print("Election Results")
    print("----------------------")
    print("Total Votes:", totalvote)
    for i in range(len(unique)):
        print(f"{unique[i]}: {percent[i]}% {candidatecount[i]}")
        # old print("Khan:", ("{:.3f}".format(100*voteKhan/Num_row)), "%  (", voteKhan, ")" )
        # old print("Correy:", ("{:.3f}".format(100*voteCorrey/Num_row)), "%  (", voteCorrey, ")" )
        # old print("Li:", ("{:.3f}".format(100*voteLi/Num_row)), "%  (", voteLi, ")" )
        #print("O'Tooley:", ("{:.3f}".format(100*voteOTooley/Num_row)), "%  (", voteOTooley, ")" )
    print("----------------------")
    print(f"Winner: {winner}")
    print("----------------------")

    with open("Pypoll_final_result_test.text", 'w') as text:
        text.write('Election Results \n')
        text.write('----------------------------------- \n')
        text.write(f'Total Votes: {totalvote} \n')
        text.write('----------------------------------- \n')
        for i in range(len(unique)):
            text.write(f'{unique[i]}: {percent[i]}% {candidatecount[i]} \n')
            #text.write(f'Correy: {("{:.3f}".format(100*voteCorrey/Num_row))}% ({voteCorrey}) \n')
            #text.write(f'Li: {("{:.3f}".format(100*voteLi/Num_row))}% ({voteLi}) \n')
            #text.write(f'O Tooley: {("{:.3f}".format(100*voteOTooley/Num_row))}% ({voteOTooley}) \n')
        text.write('----------------------------------- \n')
        text.write(f'Winner: {winner} \n')
        text.write('----------------------------------- \n')


   



