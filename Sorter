from datetime import datetime
start=datetime.now()
listo=[5,3,7,2,1,8,45,88,53,78,7632,5799,4673258,370732,379032,2489,13,124,45796,234115]
for i in range(0,len(listo)):
    for j in range(i+1,len(listo)):
        if listo[i]>listo[j]:
            listo[i],listo[j]=listo[j],listo[i]
        else:
            continue
print(listo)
end=datetime.now()
print(len(listo),"elements list sorted in ",end-start,"seconds")
