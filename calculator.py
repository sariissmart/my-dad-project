while True:
    calc = input("what calculation operatoin * - / +")
    if calc =="exit":
        break
    elif calc not in ["*","-","/","+"]:
        print("invalid operator")
        break
    user = int(input("enter first number"))
    inp = int(input("enter second number"))
    if calc == "*":
        print(user*inp)
    elif calc == "-":
        print(user-inp)
    elif calc == "/":
        print(user/inp)
    elif calc == "+":
        print(user+inp)
    else:
        print("invalid operator")
