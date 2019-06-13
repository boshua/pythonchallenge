import os
import csv
csvpath = os.path.join('..', 'Pypoll', 'election_data.csv')

total_votes = 0
cand_vote_count = {}
cand_perc = {}
winning_count = 0


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader: 
        total_votes += 1
        if row[2] not in cand_vote_count:
            cand_vote_count[row[2]] = 0
        cand_vote_count[row[2]] += 1   

for (key, value) in cand_vote_count.items():
    cand_perc[key] = round(value/total_votes * 100, 0)
    if winning_count < value:
        winning_count = value
        Winner = key
print("Election Results")
print("--------------------------")
print(f'Total Votes: {total_votes}')
print("--------------------------")
for (key,value) in cand_vote_count.items():
    print(f'{key}: {cand_perc[key]}% ({value})')
print("--------------------------")
print(f'Winner: {Winner}')
print("--------------------------")

f = open("output.txt", "a")
print("Election Results",file=f)
print("--------------------------", file=f)
print(f'Total Votes: {total_votes}', file=f)
print("--------------------------", file=f)
for (key,value) in cand_vote_count.items():
    print(f'{key}: {cand_perc[key]}% ({value})', file=f)
print("--------------------------", file=f)
print(f'Winner: {Winner}', file=f)
print("--------------------------", file=f)