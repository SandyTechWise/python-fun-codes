import time

colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']

def rainbow_print(text, color):
    print(color + text + '\033[0m')

def draw_heart():
    print("\n" * 20)
    print(" " * 8 + "❤️❤️❤️")
    print(" " * 7 + "❤️❤️❤️❤️")
    print(" " * 5 + "❤️❤️❤️❤️❤️")
    print(" " * 4 + "❤️❤️❤️❤️❤️❤️")
    print(" " * 3 + "❤️❤️❤️❤️❤️❤️❤️")
    print(" " * 2 + "❤️❤️❤️❤️❤️❤️❤️❤️")
    print(" " * 1 + "❤️❤️❤️❤️❤️❤️❤️❤️❤️")
    print(" " * 1 + "❤️❤️❤️❤️❤️❤️❤️❤️❤️")
    print(" " * 3 + "❤️❤️❤️❤️❤️❤️❤️")
    print(" " * 4 + "❤️❤️❤️❤️❤️❤️")
    print(" " * 5 + "❤️❤️❤️❤️❤️")
    print(" " * 7 + "❤️❤️❤️❤️")
    print(" " * 8 + "❤️❤️❤️")

text = "I LOVE YOU"

while True:
    draw_heart()
    for i in range(len(text)):
        rainbow_print(text[i], colors[i % len(colors)])
        time.sleep(0.5)
    time.sleep(1)
