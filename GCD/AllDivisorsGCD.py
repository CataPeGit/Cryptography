def AllDivisorsGCD(a, b):
    # Complexity: O(N) - where N = max{a,b}
    # checking for <= 0 case
    if a <= 0 or b <= 0:
        return 1

    # making sure maximum between a and b is a
    if a < b:
        a = a + b
        b = a - b
        a = a - b

    # getting all divisors of a
    divisorsA = []
    for i in range(a):
        if a % (i + 1) == 0:
            divisorsA.append(i + 1)

    # getting all divisors of b
    divisorsB = []
    for i in range(b):
        if b % (i + 1) == 0:
            divisorsB.append(i + 1)

    # getting the maximum length
    maxLenList = max(len(divisorsA), len(divisorsB))

    # going trough the longest list and finding the biggest common number (i.e. gcd)
    result = 1
    if len(divisorsA) > len(divisorsB):
        for i in range(len(divisorsA)):
            if (divisorsA[i] in divisorsB) and result < divisorsA[i]:
                result = divisorsA[i]
    else:
        for i in range(len(divisorsB)):
            if (divisorsB[i] in divisorsA) and result < divisorsB[i]:
                result = divisorsB[i]

    return result


assert AllDivisorsGCD(301, 301) == 301
assert AllDivisorsGCD(973, 301) == 7

assert AllDivisorsGCD(301, 973) == 7
assert AllDivisorsGCD(285, 30) == 15

assert AllDivisorsGCD(30, 20) == 10
assert AllDivisorsGCD(30, 20) != 5

assert AllDivisorsGCD(234234, 4566) == 6
assert AllDivisorsGCD(464642342, 7) == 1

assert AllDivisorsGCD(1729, 7) == 7
assert AllDivisorsGCD(2855, 30) == 5
