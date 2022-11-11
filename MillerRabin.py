def getSandT(n):
    # returns s and t from: n-1=2^(s) * t

    # subtracting 1 from n
    n -= 1

    # dividing n-1 by 2 until we get rest 1
    # s = numbers of divisions by 2
    # t = odd number remaining ( 1 after modulo 2 operation)

    s = 0
    while n % 2 == 0:
        s += 1
        n /= 2

    # now t == n (t equals/is n)
    return s, int(n)


def iterations(s, t):
    # we will iterate to check for all possible a
    # we also know a should be a random number
    return


def computeRSME(a, t, n):
    # computing repeated squaring modular exponentiation for a based on t
    numberOfIterations = t
    result = 1
    while numberOfIterations > 0:
        numberOfIterations -= 1
        result *= a
        if result >= n:
            result %= n
    return result


def testMillerRabin(n):
    # returns 1 if n is probably prime
    # returns 0 otherwise

    # we will see if: n-1=2^(s) * t
    # t is odd
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0

    s, t = getSandT(n)

    print(f"s={s}")
    print(f"t={t}")
    print(f"2^t={computeRSME(2, t, n)}")
    print(f"2^2*t={computeRSME(2, 2*t, n)}")
    print(f"2^4*t={computeRSME(2, 4*t, n)}")
    print(f"2^8*t={computeRSME(2, 8*t, n)}")
    print(f"2^16*t={computeRSME(2, 16*t, n)}")
    print()

    print(f"3^t={computeRSME(3, t, n)}")
    print(f"3^2*t={computeRSME(3, 2*t, n)}")
    print(f"3^4*t={computeRSME(3, 4*t, n)}")
    print(f"3^8*t={computeRSME(3, 8*t, n)}")
    print(f"3^16*t={computeRSME(3, 16*t, n)}")
    print()

    print(f"5^t={computeRSME(5, t, n)}")
    print(f"5^2*t={computeRSME(5, 2*t, n)}")
    print(f"5^4*t={computeRSME(5, 4*t, n)}")
    print(f"5^8*t={computeRSME(5, 8*t, n)}")
    print(f"5^16*t={computeRSME(5, 16*t, n)}")
    print()

    print("acum alea cu 2 la puterea bla bla: ")
    print(f"2^1={computeRSME(2, 1, n)}")
    print(f"2^2={computeRSME(2, 2, n)}")
    print(f"2^4={computeRSME(2, 4, n)}")

    print(f"2^8={computeRSME(2, 8, n)}")
    print(f"2^16={computeRSME(2, 16, n)}")
    print(f"2^32={computeRSME(2, 32, n)}")

    print(f"2^64={computeRSME(2, 64, n)}")
    print(f"2^128={computeRSME(2, 128, n)}")
    print(f"2^256={computeRSME(2, 256, n)}")

    print(f"2^512={computeRSME(2, 512, n)}")


# python MillerRabin.py
testMillerRabin(2673)
