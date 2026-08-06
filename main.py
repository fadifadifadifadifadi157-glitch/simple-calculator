while True:

 Num1=int(input("Enter the first number: "))
 Num2=int(input("Enter the second number: "))

 Choice=input("Enter the operation you want to perform (+, -, *, /): ")

 def Calculator(Num1,Num2,Choice):
    if Choice=="+":
        return Num1+Num2
    elif Choice=="-":
        return Num1-Num2
    elif Choice=="*":
        return Num1*Num2
    else:
        return Num1/Num2

 result=Calculator(Num1,Num2,Choice)
 print("The Result is:", result) 

 Again =input("Do you want to Calculate more? (Yes/No)").lower()
 if(Again =="no"):
    print("You Exit, Thank You!")
    break