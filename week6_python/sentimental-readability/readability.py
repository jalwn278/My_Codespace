from cs50 import get_string

text = get_string("Text: ")

letters = 0
sentences = 0
words = len(text.split())
l = ['!', '.', '?']
for i in text:
    if i.isalpha():
        letters += 1
    if i in l:
        sentences += 1

S = (sentences/words)*100
L = (letters/words)*100
index = round(0.0588 * L - 0.296 * S - 15.8)

if index >= 16:
    print("Grade 16+")
elif 1 <= index < 16:
    print(f"Grade {index}")
else:
    print("Before Grade 1")
