def checker():
    specialcheck=False
    alphacheck=False
    numbercheck=False
    extraspacecheck=False
    special_char="@#£_&-+()/*:;!?~`|•√π÷×¶∆€¥$¢^°={}%©®™✓[]\"\'\\"
    numbers="1234567890"
    alpha_cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passwd=input("Type the password to be validated : ")
    lispas=list(passwd)
    if len(lispas)>=5 and len(lispas)<=10 :
        lencheck=True
    else:
        print("password length should be greater than 5 and less than 10 ")
        checker()
    print(lispas)
    for j in lispas:
        print(j)
        if j in special_char:
            specialcheck=True
        if j  in alpha_cap:
            alphacheck=True
        if j in numbers:
            numbercheck=True
    if " " not in lispas:
        extraspacecheck=True
    if specialcheck != True:
        print("password should contain atleast one special character")
    if alphacheck != True:
        print("password should contain atleast one capital letter")
    if numbercheck != True:
        print("password should contain atleast one number")
    if extraspacecheck != True:
        print("password should not contain spaces")
    if specialcheck==True and alphacheck==True and numbercheck==True and extraspacecheck==True:
        print("your password is highly secured",passwd)
    else:
        checker()
            
checker()
