def Largest_prime_factor(n)
    import math
    factors = []
    
    for i in range(2, math.ceil(math.sqrt(n))):
        while n % i == 0:
            factors.append(i)
            n = n / i
    return factors[-1]

Largest_prime_factor(n = 600851475143)
