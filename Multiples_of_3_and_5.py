def Multiples_of_3_and_5(max_limit, num1, num2):
    multiplier = 1
    total = 0
    while num1*multiplier < max_limit:
        total+=num1*multiplier
        multiplier+=1
    multiplier = 1
    while num2*multiplier < max_limit:
        total+=num2*multiplier
        multiplier+=1
    multiplier = 1
    while num1*num2*multiplier < max_limit:
        total-=num1*num2*multiplier
        multiplier+=1
    return total
Multiples_of_3_and_5(1000,3,5)
