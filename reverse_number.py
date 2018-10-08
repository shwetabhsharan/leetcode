"""
reverse a number mathematically https://medium.com/@ManBearPigCode/how-to-reverse-a-number-mathematically-97c556626ec6

"""

def reverse_number(number):
    reverse = 0
    while (number > 0):
        last_digit = number % 10 # dividing number by 10 will give a remainder which will be the last digit
        reverse = (reverse * 10) + last_digit
        number = number / 10
    print reverse
reverse_number(10439402343)