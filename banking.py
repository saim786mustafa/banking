bank1 = "SSBL"
bank2 = "MSMSBL"
pin1 = 0000
pin2 = 1123
balance1 = 0
balance2 = 0
print(bank1)
print(bank2)
op = input("in which bank you want to go: ")
if op == bank1:
    pin3 = int(input("enter pin: "))
    if pin3 == pin1:
        print("=================")
        print("sucessfully login")
        print("=================")
        while True:
                print("1.transfer money")
                print("2.take loan")
                print("3.show balance")
                print("4.exit")
                opt = int(input("select option (select in 1,2,3,4): "))
                if opt == 1:
                    tr = input("who do you want to transfer: ")
                    tra = float(input(f"how many amount you want to transfer to {tr}: "))
                    if tra < 0:
                        print("enter valid amount")
                    elif tra > balance1:
                        print("insuficient funds")
                    else:
                        print("transfered sucessfully")
                        balance1 -= tra
                elif opt == 2:
                            tra2 = float(input(f"how many amount of loan you want to take "))
                            if tra2 < 0:
                                print("enter valid amount")
                            elif tra2 > 1000000:
                                print("we cant give me that much amount of loan")
                            else:
                                print("loan taked sucessfully")
                                balance1 += tra2
                elif opt == 3:
                        print(balance1)
                elif opt == 4:
                        break
                else:
                    print("incorrect pin")
                    continue    
