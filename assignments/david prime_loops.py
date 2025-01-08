num = int(input("Minimum: "))
max = int(input("Maximum: "))
while (num <= max):
    isPrime = True
    if num < 2:
        isPrime = False
    num2 = num - 1
    while(num2 > 1):
        if num % num2 == 0: 
            isPrime = False
            break 
        num2 -= 1
    if isPrime:
        print(num)
    num += 1