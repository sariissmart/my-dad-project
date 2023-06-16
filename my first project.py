def alchemist_concoction(x):
    if x % 2 == 0:
        return True
    else:
        return False


user = input("Do you want your formula odd or even?").lower()


def magic_postion():
    for magic in range(0, 21):
        if user == "even":
            if alchemist_concoction(magic):
                print(magic)
        elif user == "odd":
            if not alchemist_concoction(magic):
                print(magic)
        else:
         print("the only options is even or odd")
         break


magic_postion()
