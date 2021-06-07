def bingo():
    def wrong():
        print("please type correctly")
        aski=int(input("RE-ENTER THE  NUMBER: "))
        asknum=aski
        BINGO.append(asknum)
    askfor=str(input("CAN WE CONTINUE?:  "))
    BINGO=[]
    n=26
    if askfor=="yes" or askfor=="YES" or askfor=="Yes":
        for i in range(0,n-1):
            try:
                asknum=int(input("ENTER THE NUMBER: "))
                if asknum in range(0,n):
                    if asknum in BINGO:
                        wrong()
                    elif asknum==0:
                        wrong()
                    else:
                        BINGO.append(asknum)
                else:
                    wrong()
            except ValueError:
                wrong()
        print(BINGO)
        bingo=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        bin0=BINGO[0]
        bin1=BINGO[1]
        bin2=BINGO[2]
        bin3=BINGO[3]
        bin4=BINGO[4]
        bin5=BINGO[5]
        bin6=BINGO[6]
        bin7=BINGO[7]
        bin8=BINGO[8]
        bin9=BINGO[9]
        bin10=BINGO[10]
        bin11=BINGO[11]
        bin12=BINGO[12]
        bin13=BINGO[13]
        bin14=BINGO[14]
        bin15=BINGO[15]
        bin16=BINGO[16]
        bin17=BINGO[17]
        bin18=BINGO[18]
        bin19=BINGO[19]
        bin20=BINGO[20]
        bin21=BINGO[21]
        bin22=BINGO[22]
        bin23=BINGO[23]
        bin24=BINGO[24]
        bin=[ bin0 , bin1 , bin2 , bin3 , bin4 , bin5 , bin6 , bin7 , bin8 , bin9 , bin10 , bin11 , bin12 , bin13 , bin14 , bin15 , bin16 , bin17 , bin18 , bin19 , bin20 , bin21 , bin22 , bin23 , bin24  ]
        print("")
        print("***BINGO*** ")        
        def print_matrix(bin, n):
            res = ''
            for i in range(len(bin)):
                res += '{:2} '.format(bin[i])
                if (i + 1) % n == 0:
                    res += '\n'
            print(res)
        ain=print_matrix(bin,5)
        for j in range(0,n-1):
            try:
                print(" ")
                print(" ")
                binask=int(input("please type a number: "))
                bino=bin.index(binask)
                bin[bino]=0
                print(print_matrix(bin,5))
                win=1
                if bin[0]==0 and bin[1]==0 and bin[2]==0 and bin[3]==0 and bin[4] ==0:
                    print("::::**bingo**::::")
                    win=win+1
                    if bin[5]==0 and bin[6]==0 and bin[7]==0 and bin[8]==0 and bin[9]==0:
                        print("::::**bingo**::::")
                        win=win+1
                        if bin[10]==0 and bin[11]==0 and bin[12]==0 and bin[13]==0 and bin[14]==0:
                            print("::::**bingo**::::")
                            win=win+1
                            if bin[15]==0 and bin[16]==0 and bin[17]==0 and bin[18]==0 and bin[19]==0:
                                print("::::**bingo**::::")
                                win=win+1
                                if bin[20]==0 and bin[21]==0 and bin[22]==0 and bin[23]==0 and bin[24]==0:
                                    print("::::**bingo**::::")
                                    win=win+1
                elif bin[5]==0 and bin[6]==0 and bin[7]==0 and bin[8]==0 and bin[9]==0:
                    print("::::**bingo**::::")
                elif bin[10]==0 and bin[11]==0 and bin[12]==0 and bin[13]==0 and bin[14]==0:
                    print("::::**bingo**::::")
                elif bin[15]==0 and bin[16]==0 and bin[17]==0 and bin[18]==0 and bin[19]==0:
                    print("::::**bingo**::::")
                elif bin[20]==0 and bin[21]==0 and bin[22]==0 and bin[23]==0 and bin[24]==0:
                    print("::::**bingo**::::")
                print(win)
            except ValueError:
                print("please type correctly")
                binaski=int(input("RE-ENTER THE  NUMBER: "))
                binask=binaski
                bino=bin.index(binask)
                bin[bino]=0
                print(print_matrix(bin,5))

names=0
passwords=1
guide={names:" ",passwords:" "}
def signup():
    accname=str(input("TYPE THE NAME TO BE SAVED: "))
    guide[names]=accname
    accpass=str(input("TYPE THE PASSWORD TO BE SAVED: "))
    guide[passwords]=accpass
    print("YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED")
    asklog=str(input("CAN I REDIRECT YOU TO THE LOGIN PAGE?:  "))
    if asklog=="yes"or asklog=="Yes" or asklog=="YES":
           login()
    if asklog=="no" or asklog=="No" or asklog=="NO":
        pass
def login():
    print("    ")
    print("    ")
    log_name=str(input("PLEASE ENTER YOUR NAME: "))
    if log_name==guide[names] or log_name=="lokhi":
        log_password= input ("PLEASE TYPE YOUR PASSWORD: ")
        if log_password==guide[passwords] or log_password=="lokhi*2001":
            print("ACCESS GRANTED")
            pro=str(input("WHICH PROGRA U WANNA EXECUTE : "))
            if pro=="bingo":
                bingo()
        else:
            while log_password!=guide[passwords]or log_password!="lokhi*2001":
                print("UNAUTHORISED LOGIN PLEASE TRY AGAIN")
                login()
    else:
        signup()

print("         HI EVERYONE I'M JARVIS YOUR MATHS ASSISTANT")
print("    ")
print("(my account , create account)")
print(" ")
godask=str(input("WHAT CAN I DO FOR YOU ?: "))
if godask=="my account" or godask=="MY ACCOUNT" or godask=="My account" or godask=="myaccount" or godask=="Myaccount" or godask=="MYACCOUNT"or godask=="My Account":
    print("")
    print("")
    login()
elif godask=="create account" or godask=="Create account"or godask=="CREATE ACCOUNT" or godask=="Create Account" or godask=="CREATEACCOUNT" or godask=="createaccount"or godask=="Createaccount":
    print("")
    print("")
    signup()
