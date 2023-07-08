print("be barname mohasbe vazeyat tahsili daneshjoo khosh amadid:)")
print('Mard , zan')
gender=input("jensiat khod ra moshakhas konid.")
name=input("Esme koochake shoma chist?")
family=input("Famil shoma chist?")
print('aknoon bayad nomarate 3 dars ra vared konid.')
a=int(input("nomre dars 1 ra vared konid."))
b=int(input("nomre dars 2 ra vared konid."))
c=int(input("nomre dars 3 ra vared konid."))
d=(a+b+c)/3
gender=="Mard" or gender=="zan" 
if gender=="Mard" :
     print("vazeyat tahsili aghaye",name ,family) 
if gender=="zan" :
     print("vazeyat tahsili Khanoome",name ,family)     
if d<12 :
    print("fail")
elif d<17 :
    print("normal")
elif d<=20 :
    print("great")