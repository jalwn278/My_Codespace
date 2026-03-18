import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
else:
    if len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            f = sys.argv[2]
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

text = input("Input: ")
figlet.setFont(font=f)
print(figlet.renderText(text))
