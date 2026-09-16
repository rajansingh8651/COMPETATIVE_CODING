terms = int(input("Enter the number of terms: "))
a=0
b=1
print("Fibonacci series:")
for _ in range(terms):
    print(a,end="   ")
    c=a+b
    a=b
    b=c
