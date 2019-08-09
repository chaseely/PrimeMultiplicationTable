import sys

DEFAULT_PRIMES = 10
COLUMN_WIDTH = 5


def get_args(args):
    """
    If arguments are passed grabs the first and tries to cast to an integer.

    :param args: list of command line arguments
    :return: an integer default is 10
    """
    n = DEFAULT_PRIMES
    if args:
        try:
            n = int(args[0])
        except ValueError as e:
            print('Please provide a valid number.')
            n = -1
    return n


def is_remainder_zero(dividend, divisor):
    """
    Determines whether remainder of dividend mod divisor is zero.

    :param dividend: number to divide
    :param divisor: number to be divided by
    :return: True if dividend mod divisor equals zero otherwise False
    """
    remainder_zero = False
    if dividend % divisor == 0:
        remainder_zero = True
    return remainder_zero


def is_prime_number(num):
    """
    Determines whether a given number is a prime number.

    :param num: number to be determined
    :return: True if prime number and False otherwise
    """
    is_prime = True
    if num <= 1:
        is_prime = False
    for i in range(2, num):
        if is_remainder_zero(num, i):
            is_prime = False
            break
    return is_prime


def get_prime_numbers(n=DEFAULT_PRIMES):
    """
    Creates a list of (n) prime numbers.

    :param n: length of prime number list
    :return: list of prime numbers where length equals n
    """
    list_of_primes = []
    prime_number = 2
    while n != 0:
        if is_prime_number(prime_number):
            list_of_primes.append(prime_number)
            n -= 1
        prime_number += 1

    return list_of_primes


def build_multiplication_table(prime_numbers):
    """
    Builds a list of lists containing prime numbers and their products.

    :param prime_numbers: list of prime numbers
    """
    table = [prime_numbers]
    for prime_number in prime_numbers:
        row = [prime_number]
        for i in range(len(prime_numbers)):
            row.append(prime_number*prime_numbers[i])
        table.append(row)
    return table


def display_table(table, width=COLUMN_WIDTH):
    """
    Builds multiplication table as a string to be printed to screen.

    :param table: list of lists containing prime numbers and their products
    :param width: width between columns
    """
    table_rows = []
    for i, row in enumerate(table):
        tmp_list = []
        if i == 0:
            tmp_list.append('{:>{width}}'.format('', width=width))
        for num in row:
            tmp_list.append('{:>{width}}'.format(num, width=width))
        table_rows.append(''.join(tmp_list))

    display = '\n'.join(table_rows)
    return display


def main(args):
    n = get_args(args)
    if n == -1:
        sys.exit(1)
    primes = get_prime_numbers(n)
    table = build_multiplication_table(primes)
    display = display_table(table)
    print(display)


if __name__ == '__main__':
    main(sys.argv[1:])
