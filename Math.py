import math
a=int(input("Lotfan adad ra vared konid."))
print("+ - * / sin cos tan cot radical factorial")
c=input("amalgar ra moshakhas konid.")
if c=="+" or c=="-" or c=="*" or c=="/" :
    b=int(input("agar amalgar shoma (*,+,-,/) bood adad dovvom ra vared konid."))
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)
else :
    if c=="sin":
        print(math.sin(math.radians(a)))
    elif c=="cos":
        print(math.cos(math.radians(a)))
    elif c=="tan":
        print(math.tan(math.radians(a)))
    elif c=="cot":
        print(math.cot(math.radians(a)))
    elif c=="radical":
        print(math.sqrt(a)) 
    elif c=="factorial":
        print(math.factorial(a))