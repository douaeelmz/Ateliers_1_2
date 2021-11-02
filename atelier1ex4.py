def fib(n):
    if n<=1 :
        return 1
    else:
        return fib(n-1)+ fib(n-2)

n = int(input("enter un entier : "))
if n <= 0 :
     print("enter un entier positif ! ")
else:
    print("la série Fibonacci est : ")
for i in range(n) :
    print(fib(i))




