cuv="AS  Z SADRQWRZ"
lst=""
for i in range(0,len(cuv)):
    if(cuv[i]==" "):
        lst+=(chr(ord("-")))
    else:
        lst+=cuv[i]
print("spatiile:")
print(lst)
lst=""
for i in range(0,len(cuv)):
    if(cuv[i]!="Z" and cuv[i]!=" "):
        lst+=(chr(ord(cuv[i])+1))
    else:
        lst+=cuv[i]
print("literele:")
print(lst)
print("z cu a:")
print(cuv.replace("Z","A"))
