def f(x):
    # implicitly taking map f(x)=x^2+1
    return x * x + 1


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


def dGCDmodulo(x, y, n):
    # gcd of |x-y| and n
    modulo = x - y
    if modulo < 0:
        modulo *= -1

    return gcdEucledianAlgorithm(modulo, n)


def PollardFactoring(n):

    listOfX = [2]

    for i in range(1, 21):
        listOfX.append(f(listOfX[i - 1]) % n)

    for i in range(1, 21):
        print(f"x{i}={listOfX[i]} ")

    for i in range(1, 21):
        d = dGCDmodulo(listOfX[i * 2], listOfX[i], n)
        print(f"x{i-1}={listOfX[i * 2]} , x{i}={listOfX[i]} meaning gcd(|x-y|,n)={d}")

        if 1 < d < n:
            return d, n / d


# PollardFactoring(4087)
prim1, prim2 = PollardFactoring(7701)
print(f"Results: {prim1} and {prim2}")
# run with: python PollardFactoringAlg.py
