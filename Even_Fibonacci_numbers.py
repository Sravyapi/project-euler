def Even_Fibonacci_numbers(max_limit):
    temp = 0
    total = 0
    num1 = 0
    num2 = 1
    while temp < max_limit: 
        temp = num1 + num2 
        num1 = num2 
        num2 = temp
        if temp%2 == 0:
            total+=temp
    return total
Even_Fibonacci_numbers(4000000)   
