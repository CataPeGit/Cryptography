def gcdEucledianAlgorithm(a, b):
    # Complexity: O((logN)^2) - where a, b <= N

    # checking for <= 0 case
    if a <= 0 or b <= 0:
        return 1

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
        return gcdEucledianAlgorithm(b, a % b)


assert gcdEucledianAlgorithm(301, 301) == 301
assert gcdEucledianAlgorithm(973, 301) == 7

assert gcdEucledianAlgorithm(301, 973) == 7
assert gcdEucledianAlgorithm(285, 30) == 15

assert gcdEucledianAlgorithm(30, 20) == 10
assert gcdEucledianAlgorithm(30, 20) != 5

assert gcdEucledianAlgorithm(234234, 4566) == 6
assert gcdEucledianAlgorithm(464642342, 7) == 1

assert gcdEucledianAlgorithm(1729, 7) == 7
assert gcdEucledianAlgorithm(2855, 30) == 5
