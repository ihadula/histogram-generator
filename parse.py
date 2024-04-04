import csv

with open('./histogram.out', 'r') as file:
        lines = file.readlines()

filtered_lines = [line for line in lines if line.strip() and not line.startswith('-') and not line.startswith('Total')]

parsed_data = [line.split() for line in filtered_lines]

hits_data = []
miss_data = []

for row in parsed_data:
    latency, hits, misses = row[0], row[1], row[-1]
    hits_data.append([latency, hits])
    miss_data.append([latency, misses])

with open('hits.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(hits_data)

with open('miss.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(miss_data)

print("Data has been successfully saved to hits.csv and miss.csv")
