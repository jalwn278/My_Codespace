from cs50 import SQL

# Open database
db = SQL("sqlite:///favorite.db")

# Prompt user for favorite
favorite = input("Favorite:")

# Search for title
rows = db.excute("SELECT COUNT(*) AS n FROM favorite WHERE problem = ?", favorite)

# Get first (and only) row
row = rows[0]

# Print popularity
print(row["n"]) 
