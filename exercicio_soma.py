n1 = int(input('N1: '))
n2 = int(input('N2: '))

op = input("-Calculadora-\n"
           "+ -> Adição\n"
           "- -> Subtração\n"
           "* -> Multiplicação\n"
           "/ -> Divisão\n"
           "** -> Exponenciação\n"
           "Digite a operação: ")

match op:
    case '+': print('\nResultado =', n1 + n2)
    case '-': print('\nResultado =', n1 - n2)
    case '*': print('\nResultado =', n1 * n2)
    case '/': print('\nResultado =', n1 / n2)
    case '**': print('\nResultado =', n1 ** n2)