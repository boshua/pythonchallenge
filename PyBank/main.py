import os
import csv
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

dates = []
total = []
change = []

    


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader: 
        total.append(float(row[1]))
        dates.append(row[0])
    for i in range(1, len(total)): 
        change.append(total[i] - total[i-1])
        avg_change = sum(change) / len(change)
        max_change = max(change)
        min_change = min(change)
        max_date_change = str(dates[change.index(max_change)])
        min_date_change = str(dates[change.index(min_change)])

print("Financial Analysis")
print("-------------------------------")
print(f'Total Months: {len(dates)}')
print(f'Total: ${int(sum(total))}')
print(f'Average Change: ${round(avg_change, 2)}')
print(f'Greatest Increase in Profits: {max_date_change}  (${int(max_change)})')
print(f'Greatest Decrease in Profits: {min_date_change}  (${int(min_change)})')


f = open("output.txt", "a")
print("Financial Analysis", file=f)
print("-------------------------------", file=f)
print(f'Total Months: {len(dates)}', file=f)
print(f'Total: ${int(sum(total))}', file=f)
print(f'Average Change: ${round(avg_change, 2)}', file=f)
print(f'Greatest Increase in Profits: {max_date_change}  (${int(max_change)})', file=f)
print(f'Greatest Decrease in Profits: {min_date_change}  (${int(min_change)})', file=f)
f.close()


