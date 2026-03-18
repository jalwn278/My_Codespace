from cs50 import SQL

db = SQL("sqlite:///roster.db")

db.execute("CREATE table student (id INTEGER PRIMARY KEY, name TEXT)")

db.execute("CREATE table house (id INTEGER PRIMARY KEY AUTOINCREMENT, house TEXT, head TEXT)")

db.execute("CREATE table assignment (student_id INTEGER, house_id INTEGER, FOREIGN KEY(student_id) REFERENCES student(id), FOREIGN KEY(house_id) REFERENCES house(id))")

data = db.execute("SELECT DISTINCT house, head FROM students")
for row in data:
    db.execute("INSERT INTO house(house, head) VALUES(?,?)", row["house"], row["head"])


people = db.execute("SELECT * FROM students")
for person in people:
    db.execute("INSERT INTO student(id, name) VALUES(?, ?)", person["id"], person["student_name"])

    house = db.execute("SELECT id FROM house WHERE house = ?", person["house"])
    h_id = house[0]["id"]

    db.execute("INSERT INTO assignment(student_id, house_id) VALUES(?, ?)", person["id"], h_id)
