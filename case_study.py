import csv
import datetime
from collections import Counter, defaultdict

# 2 5 7 8
csvfile = open("crime_samples.csv", "r")
crime_data = []
for row in csv.reader(csvfile):
    crime_data.append((row[0], row[2], row[4], row[5]))

crime_data.pop(0)

# finding months with the highest number of crimes
crimes_by_month = Counter()
for row in crime_data:
    date = datetime.datetime.strptime(row[0], "%m/%d/%Y %I:%M:%S %p")
    crimes_by_month[date.month] += 1
print(crimes_by_month.most_common(3))

# locations by month on 2016
locations_by_month = defaultdict(list)
for row in crime_data:
    date = datetime.datetime.strptime(row[0], "%m/%d/%Y %I:%M:%S %p")
    if date.year == 2016:
        locations_by_month[date.month].append(row[2])
print(locations_by_month)

# most common crimes by location type in 2016
for month, locations in locations_by_month.items():
    location_count = Counter(locations)  # as container
    print(f"Month: {month}")
    print(f"Most common: {location_count.most_common(5)}")

# number of crimes by district

csvfile = open("crime_samples.csv", "r")

crimes_by_district = defaultdict(list)
for row in csv.DictReader(csvfile):
    district = row.pop("District")
    crimes_by_district[district].append(row)

for district, crimes in crimes_by_district.items():
    print(f"Disctrict number: {district}.")
    year_count = Counter()
    for crime in crimes:
        if crime["Arrest"] == "true":
            year = datetime.datetime.strptime(crime["Date"], "%m/%d/%Y %I:%M:%S %p").year
            year_count[year] += 1
    for year, number in year_count.items():
        print(f"Year: {year}, Number of crimes: {number}")

# unique crimes by city block, first crimes_by_block is needed
csvfile = open("crime_samples.csv", "r")

crimes_by_block = defaultdict(list)
for row in csv.DictReader(csvfile):
    block = row.pop("Block")
    primary_type = row["Primary Type"]
    crimes_by_block[block].append(primary_type)

# unique lst of crimes for the first block
n_state_st_crimes = set(crimes_by_block["001XX N STATE ST"])
print(list(n_state_st_crimes))
w_terminal_st_crimes = set(crimes_by_block["0000X W TERMINAL ST"])
print(list(w_terminal_st_crimes))

# gives difference between crimes for those two blocks
crime_differences = n_state_st_crimes.difference(w_terminal_st_crimes)
print(f"Differences: {list(crime_differences)}.")
