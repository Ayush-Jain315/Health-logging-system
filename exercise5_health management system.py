def getdate():
    import datetime
    return datetime.datetime.now()
x = str(getdate())
def log():
    name = input("Enter your name : ")
    log = input("If you want to add exercise write = 1 , If you want to add food write = 2\nwrite = ")
    if log == "1":
        with open(name + "exercise.txt", "a") as f:
            f.write(x + "--")
            f.write(input("enter which exercise you performed : ") + "\n")
            return ("Success")
        f.close
    if log == "2":
        with open(name + "food.txt", "a") as f:
            f.write(x + " -- ")
            f.write(input("enter which food you ate : ") + "\n")
            return ("Success")


def retrive():
    name = input("Enter your name : ")
    log = input("If you want to retrive your exercise write = 1, If you want to retrive your food write = 2\nwrite = ")
    if log == "1":
        with open(name + "exercise.txt") as f:
            print(f.read())
            return ("Success")
    if log == "2":
        with open(name + "food.txt") as f:
            print(f.read())
            return ("Success")
if __name__=='__main__':
    while(True):
        a = input("If you want to log your data write = 1\nIf you want to retrive your data write = 2\nwrite = ")
        if a == "1":
            print(log())
        elif a == "2":
            print(retrive())
        else:
            print("Wrong input try again")

        g = int(input("\nEnter 1 if you want to try it again and 2 for exit : "))
        if g == 1:
            continue
        else:
            break

