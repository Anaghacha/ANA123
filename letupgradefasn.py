def factorial(num):
    
    if num == 0 or num == 1:
        return 1
   
    else:
        fact = 1
        for i in range(1, num+1):
            fact = fact * i
        return fact

num = int(input("Enter a number: "))


result = factorial(num)
print("Factorial of", num, "is", result)
