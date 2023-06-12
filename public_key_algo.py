import numpy as np
import sys
import math


# method to find the prime values between the given range
def Find_prime_val(number1, number2):
    primes = []
    for val in range(number1, number2):
        prime_flag = True
        for val2 in range(2, val):
            if val % val2 == 0:
                prime_flag = False
        if prime_flag:
            primes.append(val)
    prime_val = np.random.choice(primes, size=2, replace=False)
    return prime_val[0], prime_val[1]


def find_pi(val1, val2):
    return (val1 - 1) * (val2 - 1)

# Finding s=gcd of an given values
def gcd(val1, val2):
    while val2 != 0:
        val1, val2 = val2, val1 % val2
    return val1


# Finding the co primes
def find_coprimes(pi):
    for val in range(pi - 3, 2, -1):
        if gcd(pi, val) == 1:
            return val
    return -1


# Finding Multiplicative inverse f
def find_multi_inv(val1, val2):
    mul_inv_val = -2
    for val in range(1, val2):
        if (val1 % val2) * (val % val2) % val2 == 1:
            mul_inv_val = val
    return mul_inv_val

# Finding the encryption value based on the message ascii and key value
def find_encrypt_val(msgToCip, key_val):
    out_val = (msgToCip ** key_val[0]) % (key_val[1])

    return out_val


# method to calculate public and private key
def rsa_key_val_gen(number1, number2):
    prime_1, prime_2 = Find_prime_val(number1, number2)
    # p,q = select_prime_val(100,250)
    prod_prime = prime_1 * prime_2
    pi = find_pi(prime_1, prime_2)
    coprime_val = find_coprimes(pi)
    mul_inv = find_multi_inv(coprime_val, pi)
    pub_key = [coprime_val, prod_prime]
    prv_key = [mul_inv, prod_prime]

    return pub_key, prv_key


def func_strList_converter(in_val):
    out_val = None
    # checks if the input is a string
    if isinstance(in_val, str):
        out_val = list(in_val)  # list() convert a string
        # to a list of character
        # checks if the input is a list

    elif isinstance(in_val, list):
        out_val = ''
        for each in in_val:
            out_val += each  # combine all characters to a string
    # print an error message if the input type is incorrect
    else:
        print('incorrect input type')
    return out_val


def func_StrAscii_Converter(in_val):
    out_val = []
    # check if the input is a list of characters
    if isinstance(in_val[0], str):
        for val in in_val:
            out_val.append(ord(val))  # ord() converts a character to ascii integer
    # check if the input is a list of integer
    elif isinstance(in_val[0], int):
        for val in in_val:
            out_val.append(chr(val))  # char() converts a ascii integer to character

    # print an error message if the input type is incorrect
    else:
        print('incorrect input type')
    return out_val
