from random import randrange, choice
from MillerRabinPrimTest import testMillerRabin

alphabet = "_abcdefghijklmnopqrstuvwxyz"  # 27 characters: a blank + 26 letters of English alphabet
# list of smaller primes
first_primes_list = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
]


from math import sqrt


def mod_inv(
    a, p
):  # returns the inverse of 'a' mod 'p' (a⁻¹ mod p) using the Extended Euclidean algorithm
    g, x, _ = egcd(a, p)
    if g != 1:
        raise Exception("No modular inverse")
    return x % p


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modular_sqrt(
    a, p
):  # function that helps us compute the quadratic congruence of the form x^2 = a mod p
    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def numericalEquivalent(unit):  # compute numerical equivalent of a unit of text
    num = 0  # ex: BED → 2 · 27^2 + 5 · 27 + 4 = 1597
    i = 2
    for char in unit:
        if char != " ":
            num += (ord(char) - 96) * (27 ** i)
        i -= 1
    return num


def decryption(encrypted_msg_units, p, q):
    # split encrypted message into units of 3 letters

    for numEquiv in encrypted_msg_units:
        xp1 = modular_sqrt(numEquiv % p, p)  # solve x^2 = numEquiv % p
        xp2 = -xp1
        xq1 = modular_sqrt(numEquiv % q, q)  # solve x^2 = numEquiv % q
        xq2 = -xq1

        N = p * q
        N1 = q
        N2 = p
        K1 = mod_inv(q, p)  # compute K1 = N1⁻¹ mod p
        K2 = mod_inv(p, q)  # compute K2 = N2⁻¹ mod q

        sol1 = (
            xp1 * N1 * K1 + xq1 * N2 * K2
        ) % N  # determine the 4 solutions modulo N=p*q
        sol2 = (xp2 * N1 * K1 + xq1 * N2 * K2) % N
        sol3 = (xp1 * N1 * K1 + xq2 * N2 * K2) % N
        sol4 = (xp2 * N1 * K1 + xq2 * N2 * K2) % N
        solutions = [sol1, sol2, sol3, sol4]

        for sol in solutions:
            if (
                sol < 27 ** 2
            ):  # turn letter values into characters to form units of 2-letter-words
                letter1 = sol // 27  # ex: sol = 128 = 4 · 27 + 20 → DT
                letter2 = sol % 27
                if letter1 == 0:
                    chr1 = "_"
                else:
                    chr1 = chr(letter1 + 96)
                if letter2 == 0:
                    chr2 = "_"
                else:
                    chr2 = chr(letter2 + 96)
                print(chr1 + chr2 + "   ", end="")
        print()


def test_with_smaller_primes(p):
    # testing if p divides smaller primes
    for divisor in first_primes_list:
        if p % divisor == 0 and divisor ** 2 <= p:
            break
        else:
            return p


def generate_prime():
    # generating large primen number p

    # num_of_bits = number of bits that prime p will have
    num_of_bits = 67

    p = 4
    while not testMillerRabin(p, 20):
        # generating random large number
        # applying Miller-Rabin primality test 20 times on p
        # primality tests passed and we return p
        # getting a prime number
        p = randrange(2 ** (num_of_bits - 1) + 1, 2 ** num_of_bits - 1)
        test_with_smaller_primes(p)

    return p


def compute_ciphertext(m, n):
    # m -> message as number between 0 and n-1
    # n -> public key of message reciever

    # computing ciphertext using formula
    formula_value = m * m % n
    return formula_value


def encrypt(text_to_encrypt):
    # getting the two characters message value
    # resulting in added values from 0(underline) to 26(z)
    value = 0
    if text_to_encrypt[0] == "_":
        value += 0
    else:
        value += (ord(text_to_encrypt[0]) - 96) * 27

    if len(text_to_encrypt) != 1:
        # avoinding eventual emty space
        if text_to_encrypt[1] == "_":
            value += 0
        else:
            value += ord(text_to_encrypt[1]) - 96

    return value


def encrypt_message(message_to_encrypt, public_key_n):
    # encrypting the message passed as a parameter with the public key parameter

    # going through the whole message
    # and encrypting substrings of 3 characters
    result = []
    start = 0
    end = 2
    i = 0
    while i < len(message_to_encrypt) / 2:

        # taking two characters from the message
        text_to_encrypt = message_to_encrypt[start:end]

        # getting numerical value of the two characters
        value = encrypt(text_to_encrypt)

        # adding to resulted encrypted message array
        # each element of the array represents two characters of the message
        result.append(compute_ciphertext(value, public_key_n))

        # iterating to the next two characters
        start += 2
        end += 2
        i += 1

    # returing resulted ciphertext
    return result


def show_encrypted_message(msg):
    r = ""
    for i in msg:
        r = r + str(i)
    return r


def get_input():
    i = input()

    for h in i:
        if h not in alphabet:
            print(
                "Try another input, the valid alphabet is: _abcdefghijklmnopqrstuvwxyz"
            )
            i = get_input()
            break
    return i


def RabinPCK():
    # demonstration of Miller-Rabin public key cryptosystem
    # Bob sends message to Alice

    print("Starting process...\n")

    # -- KEY GENERATION --

    print("Generating private and public keys...\n")
    # Note: choice(first_primes_list) can be used instead of generate_prime() if you want smaller primes

    # Alice
    # generating 2 large primes
    # (p,q) is a private key
    a_p = generate_prime()
    a_q = generate_prime()
    while a_q == a_p:
        a_q = generate_prime()
    print(f"Alice private key is: ( {a_p} , {a_q} )")

    # computing public key n
    a_n = a_p * a_q
    print(f"Alice public key is: {a_n}")

    # Bob
    # generating 2 large primes
    # (p,q) is a private key
    b_p = generate_prime()
    b_q = generate_prime()
    while b_q == b_p:
        b_q = generate_prime()

    print(f"Bob private key is: ( {b_p} , {b_q} )")

    # computing public key n
    b_n = b_p * b_q
    print(f"Bob public key is: {b_n}\n")

    # -- ENCRYPTION --

    # Alice and Bob know each other's public keys (i.e. a_n and b_n)
    # Getting unicode value from user
    # it has to be between 0 and n-1
    print("Bob, your message is: ")
    b_input_message = get_input()

    # encrypting Bob's message with Alice's public key
    encrypted_message = encrypt_message(b_input_message, a_n)

    print(
        f"Bob encrypts the message and now it is: {show_encrypted_message(encrypted_message)}\n"
    )

    # Bob sends message to Alice
    print("Bob sends the message to Alice\n")

    # -- DECRYPTION --

    # Alice decrypts Bob's encrypted message using her private key

    # displaying possible decryptions of the encrypted message
    # including the original message sent by Bob
    decryption(encrypted_message, a_p, a_q)


RabinPCK()
