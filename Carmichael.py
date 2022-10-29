from sqlalchemy import false, true


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


# utility function to find pow(x, y) under
# given modulo mod
def power(x, y, mod):
    if y == 0:
        return 1
    temp = power(x, y // 2, mod) % mod
    temp = (temp * temp) % mod
    if y % 2 == 1:
        temp = (temp * x) % mod
    return temp


# This function receives an integer n and
# finds if it's a Carmichael number
def isCarmichaelNumber(n):
    b = 2
    while b < n:

        # If "b" is relatively prime to n
        if gcd(b, n) == 1:

            # And pow(b, n-1)% n is not 1,
            # return false.
            if power(b, n - 1, n) != 1:
                return false
        b = b + 1
    return true


# ----------------------------------------------------------------------


def fermatHolds(a, number):
    # getting a to the power of number-1
    for i in range(number - 1):
        a *= a
    # testing the theorem
    if a % number == 1:
        return true
    return false


def isCharmichael(number):
    # for i in range(2, number + 1):
    # checking if parameter number and i are relatively prime
    # if gcdEA(number, i) == 1:
    #    if power(i, number - 1, number) == false:
    #        return false
    return true


def CarmichaelNumbers(bound):
    # looping trough all numbers until we reach the given bound
    # and checking if they are Carmichael numbers
    if bound <= 561:
        return []
    nums = []
    for number in range(560, bound):
        if isCarmichaelNumber(number) == true:
            nums.append(number)
    return nums


def printFermatBounded(bound):
    # printing Charmichael numbers less than bound
    print(f"Carmichael numbers less than {bound} are: ")

    nums = CarmichaelNumbers(bound)
    for i in nums:
        print(f"    {i}")


# python CarmichaelNumbers.py
printFermatBounded(600)
