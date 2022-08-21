# expression = input("Input: ")

expression = "x^2+3x+(-4)"
separated_expression = ['']
operators = ['*','/','+','-']

def separate(i):
    if expression[i-1] != '-':
        separated_expression.append('')

def main():
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    unknowns = ['x']

    for i in range(len(expression)+1):
        
        if i == 0 and expression[i] not in nums and not expression[i] == '-':
            expression = expression[:i] + '1' + expression[i:]
            i += 1

        if expression[i] == '(' and expression[i-1] not in operators:
            expression = expression[:i] + "*" + expression[i:]
            i += 1

        if expression[i] in unknowns and expression[i-1] not in nums: 
            expression = expression[:i] + "1" + expression[i:]
            i += 1

        if expression[i] in operators:
            if expression[i-1] not in operators:
                sep_eq_i += 1
                separated_expression.append('')
                separated_expression[sep_eq_i] = separated_expression[sep_eq_i] + expression[i]
                sep_eq_i += 1
                separated_expression.append('')

        separated_expression[sep_eq_i] = separated_expression[sep_eq_i] + expression[i]

    print(expression)
    print(separated_expression)

if __name__ == "__main__":
    main()


# Broken af orkar inte fixa nu
