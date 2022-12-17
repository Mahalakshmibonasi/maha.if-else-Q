basicsalary=input("enter the basic salary")
if basicsalary<=10000:
    print(basicsalary*20/100+basicsalary*80/100+basicsalary)
elif 1000<=basicsalary<=20000:
    print(basicsalary*25/100+basicsalary*90/100+basicsalary)
elif 20000<=basicsalary:
    print(basicsalary*30/100+basicsalary*95/100+basicsalary)
else:
    print("no discount")