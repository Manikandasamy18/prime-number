def is_prime(num):
    if num<=1:
        return False,count
    count = 0
    for i in range(2,int(num**0.5)+1):
     count+=1
     if num % i == 0:
        return False,count
    return True,count
try:
    num= int(input("Enter Number: "))
    prime, iterations= is_prime(num)
    if prime:
        print("It is prime")
    else:
        print("It is not prime")
    print(f"iterations :{iterations}")
except ValueError:
    print("Enter valid number")

