max = 0
while max <= 0 or max > 8:
    print("please put in a number between 1 and 8")
    max = int(input("How tall should it be? "))

for i in range(1,max+1):
    print(" "*(max-i) + "□"*i + "  "+ "□"*i)
    i+=1