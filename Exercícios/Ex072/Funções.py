def calculadora(a, b, c='+'):
    """
    Performs basic arithmetic operations on two numbers.

    :param a: (float) first number.
    :param b: (float) second number.
    :param c: (str, optional): The operation to perform. Default is addition ('+').
    Valid operations are '+', '-', 'x' (multiplication), and '/' (division).

    :return: (float) The result of the specified operation.
    """
    if c == '+':
        return a + b
    if c == '-':
        return a - b
    if c == 'x':
        return a * b
    if c == '/':
        return a / b


def tabuada(a):
    """
    Prints the multiplication table for a given number.

    :param a: (int) number for which the multiplication table is generated.
    :return: no return
    """
    print(f'Tabuada do {a}')
    for c in range(1, 11):
        print(f'{a} x {c} = {a*c}')


def par_impar(a):
    """
    Determines whether a given number is even or odd and prints the result.

    :param a: (int) number to check for parity.
    :return: no return
    """
    if a % 2 == 0:
        print(f'O número {a} é par')
    else:
        print(f'O número {a} é impar')


def num_primos(a):
    """
    Determines whether a given number is prime and prints the result.
    :param a: (int) number to check for primality.
    :return:
    """
    cont = 0
    for c in range(1, a+1):
        if a % c == 0:
            cont += 1
    if cont == 2:
        print(f'O número {a} é primo, foi divisível {cont} vezes.')
    else:
        print(f'O número {a} não é primo, foi divisível {cont} vezes')


def factorial(num, mostar=False):
    """
     Calculates the factorial of a given number.

    :param num: (int) number for which to calculate the factorial.
    :param mostar: (bool, optional) Whether to display the steps of the calculation. Default is False.
    :return: (int) The factorial of the given number.
    """
    fat = 1
    for i in range(num, 0, -1):
        if mostar:
            if i == 1:
                print(f'{i} =', end='')
            else:
                print(f'{i} x ', end='')
        fat *= i
    return fat
