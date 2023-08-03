#!/usr/bin/env python3


# adding_squares
def adding_squares(x, y):
    """return sum of squares of two numbers

    Args:
        x (int): first number
        y (int): second number

    Returns:
        int: Sum of squares of x and y
    """
    return sum([x**2, y**2])


print(adding_squares(4, 3))


def m_word_count(string):
    """counts number words starts with 'm' letter in string

    Args:
        string (str): input as a string

    Returns:
        int: number of letter occurence
    """
    words = string.split()
    count = 0
    for letter in words:
        if letter[0].lower() == "m":
            count += 1
    return count


sentence = "Hello, My dearest Margaret. What a nice suprise."
print(m_word_count(sentence))


def vowel_count(string):
    """counts vowels which are on string"""
    count = 0
    vowels = ["a", "e", "i", "o", "u", "y"]
    for i in range(len(string)):
        if string[i] in vowels:
            count += 1
    return count


string_example = "Harry Potter"
print(vowel_count(string_example))


def continuee(lst):
    for i in lst:
        if i % 2 == 0:
            continue
        print(i)


# so it gives 1, 1, 3 as example [1, 1, 2, 3]


def breakit(lst):
    for i in lst:
        if i % 2 == 0:
            break
        print(i)


# so it gives 1, 1 as example d1, 1, 2, 3]


def date_extractor(date):
    date_splitted = date.split("/")
    print(date_splitted)


date_extractor("5/12/2022")
