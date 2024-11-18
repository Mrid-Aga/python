import itertools
while True:
    try:
        start = int(input("Where should it start looking for primes? "))
        break
    except (MemoryError, OverflowError):
        print("Too big for our system or for Python. Try a smaller number")
    except ValueError:
        print("Not a number. Try again")
while True:
    try:
        end = int(input("Where should it stop looking? "))
        break
    except (MemoryError, OverflowError):
        print("Too big for our system or for Python. Try a smaller number")
    except ValueError:
        print("Not a number. Try again")
while True:
    try:
        num_list=list(range(2,end+1))
        break
    except (MemoryError, OverflowError):
        print("Too big for your system or for Python. Try a smaller number")
        end = int(input("Where should it stop looking? "))
    except ValueError:
        print("Not a number. Try again")
        end = int(input("Where should it stop looking? "))
num_list=list(range(2,end+1))
try:
    combinations = (list(itertools.product(num_list, num_list)))
except (MemoryError, OverflowError):
    print("Too big for your system or for Python. Try a smaller number")
    end = int(input("Where should it stop looking? "))
    num_list=list(range(2,end+1))
multiplications = []
for tuples in combinations:
    try:
        if tuples[0]*tuples[1]<=end:
            mult = tuples[0]*tuples[1]
            multiplications.append(mult)
    except (MemoryError, OverflowError):
        print("Too big for your system or for Python. Try a smaller number")
    except ValueError:
        print("Not a number. Try again")

for i in multiplications:
    if i in num_list:
        num_list.remove(i)
print(num_list)