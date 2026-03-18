from cs50 import get_float

while True:
    try:
        change = get_float("Change: ")
        if change > 0:
            break
    except ValueError:
        print("Please input a positive number")

coins = 0
cents = round(change * 100)

while cents >= 25:
    cents = cents - 25
    coins += 1
while cents >= 10:
    cents = cents - 10
    coins += 1
while cents >= 5:
    cents = cents - 5
    coins += 1
while cents >= 1:
    cents = cents - 1
    coins += 1

print(f"{coins}")
