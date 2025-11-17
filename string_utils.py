def split_before_each_uppercases(formula):
    if not formula:
        return []  

    split_formula = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
    split_formula.append(formula[start:])
    return split_formula



def split_at_first_digit(formula):
    digit_location = -1
    for i in range(len(formula)):
        if formula[i].isdigit():   
            digit_location = i
            break
        
    if digit_location == -1:  
        return (formula, 1)
    else:
        prefix = formula[:digit_location]
        number = int(formula[digit_location:])
        return (prefix, number)
