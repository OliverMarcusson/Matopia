# equation = input("Input: ")

def main():
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    operators = ['*','/','+','-']

    unknowns = ['x']
    equation = "x*2x*-x-4(3x+2)"
    separated_equation = ['']
    sep_eq_i = 0

    for i in range(len(equation)+1):
        
        if i == 0 and equation[i] not in nums and not equation[i] == '-':
            equation = equation[:i] + '1' + equation[i:]

        if equation[i] == '(' and equation[i-1] not in operators:
            equation = equation[:i] + "*" + equation[i:]

        if equation[i] in unknowns and equation[i-1] not in nums: 
            equation = equation[:i] + "1" + equation[i:]

        if equation[i] in operators:
            if equation[i-1] not in operators:
                sep_eq_i += 1
                separated_equation.append('')
                separated_equation[sep_eq_i] = separated_equation[sep_eq_i] + equation[i]
                sep_eq_i += 1
                separated_equation.append('')

        separated_equation[sep_eq_i] = separated_equation[sep_eq_i] + equation[i]

    print(equation)
    print(separated_equation)

if __name__ == "__main__":
    main()


# Broken af orkar inte fixa nu
