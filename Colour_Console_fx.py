import random
from sty import fg
# Sty is a python package that allows you to change the colour of text in the console
# You can install it by running the command: pip install sty
# You can find the documentation here: https://sty.mewo.dev/

def generateRGB(): # Generates a random RGB value
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue

def generateColour(red, green, blue):# Generates a colour using the RGB values
    return fg(red, green, blue)

red, green, blue = generateRGB()
colour = generateColour(red, green, blue)

print (red, green, blue)# Prints the RGB values
print(colour, "I'm randomly changing colours muahahahahahaha!!", fg.rs)