from sqlalchemy import false, true


def congruentExpression(b, number):
    # checking if fermat expression holds
    cr = pow(b, number - 1)
    if cr % number == 1:
        return true
    return false


def gcdEA(a, b):
    # checking for == 0 case
    if a == 0:
        return b

    if b == 0:
        return a

    # making sure maximum between a and b is a
    if a < b:
        a = a + b
        b = a - b
        a = a - b

    # when the greater or equal number (a in our case) mod the other number(b in our case) equals zero
    # the algorithm ends and the result is the other number(b in our case)
    # else recurse with a = b and b = a % b
    if a % b == 0:
        return b
    else:
        return gcdEA(b, a % b)


def isComposite(number):
    # checking if number is composite
    if number <= 3:
        return False
    if number % 2 == 0:
        return True
    i = 5
    while i * i <= number:

        if number % i == 0:
            return True
        i += 2
    return False


def isCarmichael(number):
    # checking if number is Carmichael

    # Number has to be composite
    if not isComposite(number):
        return false

    for i in range(2, number + 1):
        # checking if parameter number and i are relatively prime
        # and Fermat's expression holds
        if gcdEA(number, i) == 1:
            if congruentExpression(i, number) == false:
                return false
    return true


def CarmichaelNumbers(bound):
    # looping trough all numbers until we reach the given bound
    # and checking if they are Carmichael numbers
    if bound <= 561:
        return []
    nums = []
    for number in range(560, bound):
        if isCarmichael(number) == true:
            nums.append(number)
    return nums


def printFermatBounded(bound):
    # printing Charmichael numbers less than bound

    print(f"Carmichael numbers less than {bound} are: ")
    nums = CarmichaelNumbers(bound)
    if len(nums) == 0:
        print("    There are none.")
        return
    for i in nums:
        print(f"    {i}")


# python CarmichaelNumbers.py
printFermatBounded(15842)
printFermatBounded(600)
printFermatBounded(561)
