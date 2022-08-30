#grade of a student
#read marks of 3 subjects(100)
#percentage=(total mark/300)*100
# >=90   ->grade A+
# 80-89  ->grade A
# 70-79  ->grade B+
# 60-69  ->grade B
# 50-59  ->grade C+
# 40-49  ->grade C
# 30-39  ->grade D+
# <30    ->failed


m=int(input("enter the mark in maths"))
e=int(input("enter the mark in english"))
h=int(input("enter the marks in hindi"))
if m<=100 and e<=100 and h<=100:
    t=m+e+h
    print("Total mark=",t)
    p=(t/300)*100
    print("Percentage of marks=",p)
    if p>=90:
        print("Grade A+")
    elif p>=80:
        print("grade A")
    elif p>=70:
        print("grade B+")
    elif p>=60:
        print("grade B")
    elif p>=50:
        print("grade C+")
    elif p>=40:
        print("grade C")
    else:
        print("failed")
else:
    print("wrong mark")
