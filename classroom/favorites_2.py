import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    counts = {}

    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1 #counts["python"] += 1
        else:
            counts[favorite] = 1

        #try:
            #counts[favorite] += 1
        #except KeyError:
            #counts[favorite] = 1
for favorite in sorted(counts, key = counts.get, reverse = True):
    print(f"{favorite}: {counts[favorite]}")
