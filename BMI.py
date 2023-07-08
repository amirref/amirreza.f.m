import math 
print("be barname mohasbe vazeyat salamat badan (BMI) khosh amadid:)")
print('baraye mohasebe BMI shoma man be "ghad" va "vazn" shoma niaz daram ')

a=int(input("vazn khod ra vared konid.(Kilo Geram) " ))
b=float(input("ghad khod ra vared konid.(metr) "))
c=b*b
BMI=a/c
print(BMI)
if BMI<=18.5 :
    print("underweight (kambood vazn)")
elif 18.5<=BMI<=24.9 :
    print("normal")
elif 24.91<=BMI<=29.9 :
    print("overweight (ezafe vazn)")
elif 29.91<=BMI<=34.9 :
    print("Obese (chagh)")
elif 35<=BMI :
    print("extremely obese (Kheili chagh)")
    print("be fekre salamate khod bashid.")   
print("* * * * * * * * * * * *")
print("Good Lock")    
print("* * * * * * * * * * * *")