def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fuzz'
    if input % 5 == 0:
        return 'duzz'
    return input


print(fizz_buzz(int((input('enter number: ')))))
