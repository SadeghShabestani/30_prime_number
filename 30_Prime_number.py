import termcolor2


def prime_number():
    number = int(input("Enter Number: "))
    if number % 2 == 1:
        return termcolor2.colored("True", color="green")
    else:
        return termcolor2.colored("False", color="red")


print(prime_number())


def number_between():
    a = int(input("Enter First Number: "))
    b = int(input("Enter second Number: "))
    for i in range(a, b):
        if i % 2 == 1:
            print(i)


number_between()
