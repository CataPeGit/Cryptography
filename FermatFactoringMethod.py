from math import isqrt, sqrt


def squareRoot(a):
    # get the square root of parameter a
    return sqrt(a)


def is_square(apositiveint):
    # check if number is perfect square
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def isPerfectSquare(x):

    # if x >= 0,
    if x >= 0:
        sr = int(sqrt(x))
        # sqrt function returns floating value so we have to convert it into integer
        # return boolean T/F
        return (sr * sr) == x
    return False


def findSandT(n, tzero):
    # a = square root of n
    # where n = t^2 * s^2
    # returns s and t as integers

    # loop until we find integer t
    for s in range(1, 15):
        t = tzero + s

        # t = t^2 - n
        t = t * t - n

        print(f"Iteration {s} has t = {t}")

        if is_square(t):
            print(f"and {s*s} is perfect square!")
            return t, tzero + s
    return


def checkResult_GetPrimeFactors(n, s, t):

    if n == s * s - t * t:
        prime1 = t + s
        prime2 = t - s

        return prime1, prime2


def fermatFactoringMethod(n):

    # getting a t0 = square root of n
    tzero = isqrt(n)

    print(f"t0 is : {tzero}")

    # n = t^2 * s^2
    s, t = findSandT(n, tzero)

    print(f"s = {s}")
    print(f"t = {t}")

    prime1 = t + s
    prime2 = t - s

    if prime1 < prime2:
        return prime1, prime2
    else:
        return prime2, prime1


prime1, prime2 = fermatFactoringMethod(9699)  

print(f"The two factors are {prime1} and {prime2}")

print()

prime1, prime2 = fermatFactoringMethod(7701)
print(f"The two factors are {prime1} and {prime2}")
# run with: python FermatFactoringMethod.py
