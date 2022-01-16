a=int(input("Enter your Percentage\nFrom 0 to 100"))
# a=int(input("Enter your Percentage\tFrom 0 to 100"))
if not(a>=40 and a<=100):
    print("Invalid Percentage")
elif a>=90:
    print("Outstanding Result")    
elif a>=80:
    print("You scored Distinction")
elif a>=70:
    print("You scored First Division")
elif a>=60:
    print("You scored Second Division")    
elif a>=40:
    print("You scored Third Division")       

