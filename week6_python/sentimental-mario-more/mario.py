while True:
    try:
        height = int(input("Height: "))
        if 0 < height < 9:
            break
    except ValueError:
        print("Please input an integer.")

for i in range(1,height+1):
    spaces = " "*(height - i)
    hashes = "#"*i
    print(spaces+hashes, end="")
    print("  ", end="")
    print(hashes)
