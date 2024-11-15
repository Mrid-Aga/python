import itertools
start = int(input("Where should it start looking for primes? "))
end = int(input("Where should it stop looking? "))
num_list=list(range(2,end+1))

combinations = (list(itertools.product(list(range(2,end)), num_list)))
multiplications = []

for tuples in combinations:
    mult = tuples[0]*tuples[1]
    multiplications.append(mult)

for i in multiplications:
    if i in num_list:
        num_list.remove(i)
print(num_list)
