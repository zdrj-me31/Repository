#!/usr/bin/env python3


def prime_finder(number):
    lst = []  # creates a new list
    for num in range(1, number + 1):
        if num > 1:
            # if num for example can be divisible by 1, itself and anothers then break and goes to another num from line 11,
            # if two first options only num adds to lst
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                lst.append(num)
    return lst


print(prime_finder(23))


def prime_finder(n):
    """creates a list of prime numbers from range of n number, for example if number can be divisble by 1,
    and by itself it adds to list, if more than mentioned two options goes back to loop through range of input number

    Args:
        n (int): number from which range we find prime numbers

    Returns:
        list : list of prime numbers
    """
    answer = []
    for x in range(2, n + 1):
        prime = True
    for i in range(2, x):
        if x != i and x % i == 0:
            prime = False
    if prime:
        answer.append(x)
    return answer
