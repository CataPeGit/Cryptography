from random import randrange


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


def computeRSME(a, t, n):
    # computing modular exponentiation for a based on t
    # this is pretty much pow(a,t,n)
    numberOfIterations = t
    result = 1
    while numberOfIterations > 0:
        numberOfIterations -= 1
        result *= a
        if result >= n:
            result %= n
    return result


def checkSequence(a, s, t, n):
    # this checks the sequence that looks like:
    # a^t, a^(2*t), a^(2^2(t)), a^(2^(3) * (t)), ... , a^(2^(s) * (t))

    # check if first number is 1 otherwise
    # and save it as previous for later use

    prev = pow(a, t, n)
    if prev == 1 or prev == n - 1:
        return 1

    # going trough all values in the sequence
    # checking if the current is 1 and previous is -1
    repeatedSquare = 1
    for i in range(s):
        prev = prev * prev % n
        if prev == n - 1:
            return 1

    # getting to this point means n is composite
    return 0


def testMillerRabin(n, k):
    # returns 1 if n is probably prime
    # returns 0 otherwise

    # cases <= 1 and even numbers

    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0:
        return 0

    # we will see if: n-1=2^(s) * t
    # t is odd
    s, t = getSandT(n)

    # computing and checking sequence in Miller-Rabin test --> iterating k times
    for i in range(k):

        # a should be a random number such that: 1 < a < n - 1
        # generating pseudo random a
        a = randrange(2, n - 2)

        if checkSequence(a, s, t, n) == 0:
            # after checking we get: number is composite
            return 0

    # after checking we get: number is probably prime
    return 1


# python MillerRabin.py
nums = 500
iterations = 4
print(f"Checking first {nums} numbers for primality: ")

if testMillerRabin(2, iterations) == 1:
    print(f"2 is prime!")


for i in range(1, nums, 2):
    if testMillerRabin(i, iterations) == 1:
        print(f"{i} is prime!")
