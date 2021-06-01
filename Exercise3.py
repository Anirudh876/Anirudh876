i = 65

while(True):
    inp = int(input("ENter an number"))
    if inp == i:
        print("Congrates!!! KEEP up it")
        break
    elif inp > i:
        print("Decrease")
    elif inp < i:
        print("Increase")
    else:
        print("try aganin")
        continue

