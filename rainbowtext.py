import time
import sys
from termcolor import colored
from pyfiglet import Figlet

def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    figlet = Figlet(font='block')
    for color in colors:
        sys.stdout.write("\033c") # Clear the screen
        colored_text = colored(figlet.renderText(text), color)
        print(colored_text)
        time.sleep(1)

if __name__ == "__main__":
    rainbow_text("TEXT")
