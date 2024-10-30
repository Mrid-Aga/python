def quadratic(a,b,c):
    answers = []
    x_pos = (-b+(b**2-4*a*c)**0.5)/(2*a)
    pos_string = str(x_pos).replace(".","")
    if pos_string.isnumeric():
        answers.append(x_pos)
    else:
        print("not solvable")
        return
    x_neg = (-b-(b**2-4*a*c)**0.5)/(2*a)
    neg_string = str(x_neg).replace(".","")
    if pos_string.isnumeric():
        answers.append(x_pos)
    else:
        print("unsolvable")
        return
    return (answers)

print(quadratic((int(input("a: "))),(int(input("b: "))),(int(input("c: ")))))