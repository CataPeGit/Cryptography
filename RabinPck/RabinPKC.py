from random import randrange
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
    num_of_bits = 64

    p = 4
    while not testMillerRabin(p, 20):
        # generating random large number
        # applying Miller-Rabin primality test 20 times on p
        # primality tests passed and we return p
        # print("cox")
        # getting a prime number
        p = randrange(2 ** (num_of_bits - 1) + 1, 2 ** num_of_bits - 1)
        test_with_smaller_primes(p)

    return p


def compute_ciphertext(m, n):
    # computing ciphertext using formula
    # m -> message as number between 0 and n-1
    # n -> public key of message reciever
    return m * m % n


def encrypt_message(message_to_encrypt, public_key_n):
    # encrypting the message passed as a parameter with the public key parameter

    # getting the message ascii value - 96
    # resulting in added values from 0(underline) to 26(z)
    ascii_value = 0
    for cha in message_to_encrypt:
        if cha == "_":
            continue
        else:
            ascii_value += ord(cha) - 96
    # returing computed ciphertext
    return compute_ciphertext(ascii_value, public_key_n)


# def encrypt_message(p, q, n, encrypted_message):
# decrypting message
# (p,q) -> private key
# n -> public key


def RabinPCK():
    # demonstration of Miller-Rabin public key cryptosystem
    # Bob sends message to Alice

    # -- KEY GENERATION --

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
    b_input_message = input("Bob, your message is: ")

    # encrypting Bob's message with Alice's public key
    encrypted_message = encrypt_message(b_input_message, a_n)

    print(f"Bob encrypts the message and now it is: {encrypted_message}\n")

    # Bob sends message to Alice
    print("Bob sends the message to Alice\n")

    # -- DECRYPTION --

    # Alice decrypts Bob's encrypted message using her private key
    # decrypted_message = encrypt_message(a_p, a_q, a_n, encrypted_message)


print("Starting process...\n")
RabinPCK()
