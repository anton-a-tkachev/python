# CSV parsing
import csv
from datetime import datetime

# path = "d:\Documents\Coding\Python\google_stock_data.csv"
# file = open(path)
# for line in file:
#     print(line)

# path = "d:\Documents\Coding\Python\google_stock_data.csv"
# dataset = [line.strip().split(',') for line in open(path)]
# print(dataset[0])

# path = "d:\Documents\Coding\Python\google_stock_data.csv"
# file = open(path, newline = '')
# reader = csv.reader(file)

# header = next(reader)
# data = [row for row in reader]

# print(header)
# print(data[0])

# Parse the CSV-file
path = "d:\Documents\Coding\Python\google_stock_data.csv"
file = open(path, newline = '')
reader = csv.reader(file)

header = next(reader)
data = []

for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price  = float(row[1])
    high_price  = float(row[2])
    low_price   = float(row[3])
    close_price = float(row[4])
    volume      =   int(row[5])
    adj_close   = float(row[6])
    data.append([date, open_price, high_price, low_price, close_price, volume, adj_close])

# print(header)
# print(data[0])

# Compute and store daily stock returns
returns_path = "d:\Documents\Coding\Python\google_returns.csv"
file = open(returns_path, 'w', newline = '')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    yesterdays_row = data[i+1]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price)/yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
