import time

def walk(walkcount):
    cap = "    👑"
    head = "    😎"
    body = "    👕🌹"
    leg = "    👖"
    frontshoe = "  👟   👞"
    middleshoe = "    👟"
    backshoe = "   👞 👟"

    for i in range(walkcount):
        if (i % 3 == 0):
            print(i*" "+cap)
            print(i*" "+head)
            print(i*" "+body)
            print(i*" "+leg)
            print(i*" "+middleshoe)
        elif (i % 3 == 1):
            print(i*" "+cap)
            print(i*" "+head)
            print(i*" "+body)
            print(i*" "+leg)
            print(i*" "+frontshoe)
        else:
            print(i*" "+cap)
            print(i*" "+head)
            print(i*" "+body)
            print(i*" "+leg)
            print(i*" "+backshoe)

        time.sleep(0.2)
        print("\033c")

    print(walkcount*" "+cap)
    print(walkcount*" "+head)
    print(walkcount*" "+body+"I Love You!")
    print(walkcount*" "+leg)
    print(walkcount*" "+middleshoe)


if __name__ == '__main__':
    walk(18)
