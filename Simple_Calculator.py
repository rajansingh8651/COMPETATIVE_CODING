num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))
operator=input("Enter your operator number : ")
if operator=="+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operator =="-":
    print(f"{num1} - {num2} = {num1-num2}")
elif operator=="*":
    print(f"{num1} * {num2} = {num1*num2}")
elif operator=="/":
    print(f"{num1} / {num2} = {num1/num2}")
elif operator=="//":
    print(f"{num1} // {num2} = {num1//num2}")
elif operator=="%":
    print(f"{num1} % {num2} = {num1%num2}")
elif operator=="**":
    print(f"{num1} ** {num2} = {num1**num2}")
else:
    print("Envalid operator")