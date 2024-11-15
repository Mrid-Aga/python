start = 0
years = 0
while True:
    try:
        start = int(input("How many lammas to start off with? "))
        start_permanant = start
    except ValueError:
        print("please put in a number bigger than 9")
    if start <9:
        print("please put in a number bigger than 9")
    else:
        break
end = int(input("What population do you want it to stop at?"))
while start < end:
    start+=(start/3-start/4)
    print("Population"+start)
    years += 1
print("Start Size: "+str(start_permanant))
print("Current Size: "+str(start))
print("Years: "+years)

