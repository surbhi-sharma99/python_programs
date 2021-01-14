primes_till_100=[]
prime_no=1
for num in range(2,101):
    for j in range(2,num):
        if num%2:
            primes_till_100.append(num)
    
        
for prime in primes_till_100:
    print(prime)
