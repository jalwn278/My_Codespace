phrase = input("Give me a string: ")

for i in range(0, len(phrase), 2):
    print(phrase[i], end="")
print("")

for i in range(1, len(phrase)-1):
    print(phrase[i],end="")
print("")

for character in phrase:
    print(character,end="")
print("")

for character in phrase[1:]:
    print(character,end="")
print("")

j = 0
while j < len(phrase):
    print(phrase[j],end="")
    j += 1
print("")

for i in range(len(phrase)-1, -1, -1):
    print(phrase[i],end="")
print("")
