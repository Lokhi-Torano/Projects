#import_statements
import random as ran
#data_base
alpha_small=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpha_caps=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#swapper
def swapper(meta_list):
    if len(meta_list)%2==0:
        #even
        print("eve")
        len_half=int(len(meta_list)/2)
        for i in range(0,len_half):
            temp=meta_list[i]
            meta_list[i]=meta_list[i+len_half]
            meta_list[i+len_half]=temp
        return meta_list
    else:
        #odd
        len_half_1=int((len(meta_list)/2))
        for i in range(0,len_half_1):
            temp=meta_list[i]
            meta_list[i]=meta_list[i+len_half_1+1]
            meta_list[i+len_half_1+1]=temp
        return meta_list

#encryption
def encryption():
    meta_list=[]
    print("welcome to encryption sector")
    text_input=str(input("type your text : "))
    list_text_input=list(text_input)
    for i in range (0,len(list_text_input)):
        if list_text_input[i]!=" ":
            print("hey",list_text_input[i])
            meta_list.append(list_text_input[i])
        else:
            continue
    swapped=swapper(meta_list)
    print(swapped)
    random=ran.randint(10,15)
    print("rand",random)
    finlist=[]
    for o in range(0,len(swapped)):
        for i in range(0,len(alpha_small)):
            if swapped[o]==alpha_small[i]:
                print("hello")
                finlist.append(alpha_small[i+random-1])
    print("your passcode is :",random)
    fintext="".join(finlist)
    print("encrypted text is",fintext)
                
            
#greet welcome to pycrypt
print("WELCOME TO PYCRYPT")
print("1.ENCRYPTION")
print("2.DECRYPTION")
print("3.EXIT")
ask_entry=int(input("type your choice : "))
if ask_entry==1:
    encryption()
if ask_entry==2:
    decryption()
if ask_entry==3:
    exit()
