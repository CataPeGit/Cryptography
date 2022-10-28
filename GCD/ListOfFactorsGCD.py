def gcdListOfFactors(a, b):
    # Complexity: O(N) - where N = max{a,b}

    # checking for <= 0 case
    if a <= 0 or b <= 0:
        return 1

    # making sure maximum between a and b is a
    if a < b:
        a = a + b
        b = a - b
        a = a - b

    max = 1
    for i in range(a):
        if a % (i + 1) == 0 and b % (i + 1) == 0 and max < (i + 1):
            max = i + 1
    return max


assert gcdListOfFactors(301, 301) == 301
assert gcdListOfFactors(973, 301) == 7

assert gcdListOfFactors(301, 973) == 7
assert gcdListOfFactors(285, 30) == 15

assert gcdListOfFactors(30, 20) == 10
assert gcdListOfFactors(30, 20) != 5

assert gcdListOfFactors(234234, 4566) == 6
assert gcdListOfFactors(464642342, 7) == 1

assert gcdListOfFactors(1729, 7) == 7
assert gcdListOfFactors(2855, 30) == 5
