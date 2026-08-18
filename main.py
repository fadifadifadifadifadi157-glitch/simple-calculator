def Calculator(Num1, Num2, Choice):
    if Choice== "+":
        return Num1 + Num2
    elif Choice=="-":
        return Num1 - Num2
    elif Choice == "*":
        return Num1*Num2
    elif Choice=="/":
        if Num2==0:
            return "Cannot divide by zero!"
        return Num1/Num2
    elif Choice =="%":
        if Num2== 0:
            return "Cannot divide by zero!"
        return Num1%Num2
    elif Choice== "//":
        if Num2 ==0:
            return "Cannot divide by zero!"
        return Num1 //Num2
    elif Choice =="**":
        return Num1** Num2
    else:
        return "Invalid operation!"


while True:
    try:
        Num1 =int(input("Enter the first number: "))
        Num2 = int(input("Enter the second number: "))
    except:
        print("Please enter numbers only!")
        continue

    Choice =input("Enter operation (+, -, *, /, %, //, **): ")

    if Choice not in ["+", "-", "*","/", "%", "//", "**"]:
        print("Invalid operation!")
        continue

    result = Calculator(Num1, Num2, Choice)
    print("The Result is:", result)

    Again = input("Do you want to calculate more? (Yes/No): ").lower()

    if Again =="no":
        print("You Exit, Thank You!")
        break

    if Again !="yes":
        print("Please enter Yes or No!")
