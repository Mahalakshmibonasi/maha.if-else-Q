a=int(input("enter the num"))
if a>=80:
    print("grade A")
elif a<=80 and a>=60:
    print("grade B")
elif a<=60 and a>=50:
    print("grade C")
elif a<=50 and a>=45:
    print("grade D")
elif a<=45 and a>=25:
    print("grade E")
elif a<=25:
    print("fail")
else:
    print("nothing")