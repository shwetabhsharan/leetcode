def find_prime(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    range_list = range(n+1)[1:]

    for number in range_list:
        factorial = facto(number)
        print number, factorial,  number % factorial
        if number == (factorial % number):
            print number

def facto(number):

    number_list = range(number+1)[1:]
    final = 1
    for no in number_list:
        final = final*no
    return final

find_prime(3)