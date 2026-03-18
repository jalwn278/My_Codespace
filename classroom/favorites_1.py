import csv

with open('favorites.csv', 'r') as file:
    reader = csv.DictReader(file)
    #next(reader) #skip first line dictionary will automately skip the first line because it know who is itself

    #for row in reader:
        #print(row["language"])
    #count the number
    scratch, python, c = 0, 0, 0
    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "Python":
            python += 1
        elif favorite == "C":
            c += 1

print(f"Python: {python}")
print(f"C: {c}")
print(f"Scratch: {scratch}")

