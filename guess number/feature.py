import random
from random import choice


def get_range_number():
    """
take the guessed numbers distance"""
    global range_1, range_2
    while True:
        range_1 = input("choose start number range : ")
        try:
            range_1 = int(range_1)
            try:
                range_2 = input("choose end number range : ")
                range_2 = int(range_2)
            except:
                print("input only the numeric form!!!")
                continue
        except:
            print("input only the numeric form!!!")
            continue
        else:
            if range_1 < range_2 and (range_2-range_1) >= 9:
                break
            else:
                print(
                    "the starting number must be less than the final digit and the \
                    minimum distance is 10 digits.")


def get_guess_numbers():
    numbers = {}
    """take the guessed numbers and the numbers associated with these numbers."""
    use_number = []
    while True:
        number = random.randint(range_1, range_2)
        for i in range(2, range_2):
            if (number % i == 0 or i % number == 0) and (i != number):
                use_number.append(i)
        if use_number or number == 0:
            break
        break
    numbers['guess_number'] = number
    numbers['list_use_number'] = use_number
    return numbers


def zero_number(list_num):
    """generate several statements related to zeros."""
    str_zero = [
        "this number is neither a positive number nor a negative number",
        "multiplying by this number yields this number as well",
        "the result of division by this number is undefined",
        "is an even number",
    ]
    if list_num:
        get_str = choice(list_num)
        str_hint = "- " + str_zero[get_str]
        list_num.remove(get_str)
    else:
        str_hint = "- this number is not a prime number"
    return str_hint


def get_primes(number):
    """yields several statements regarding large prime numbers"""
    another_number_1 = choice(
        [x for x in range((number-random.randint(1, 10)), number)])
    another_number_2 = choice(
        [x for x in range(number, (number+random.randint(1, 10)))])
    str_hint = "- this number satisfies the inequality " + \
        str(another_number_1) + " <= ??? <= " + str(another_number_2)
    return str_hint


def clue_formula(number, use_number, temp, list_num_zero):
    """formula for taking hints."""
    if number == 0:
        str_hint = zero_number(list_num_zero)
    elif use_number:
        get_use_number = choice(use_number)
        if number % get_use_number == 0 and get_use_number not in temp:
            a = get_use_number
            b = int(number/get_use_number)
            str_hint = "- this number satisfies the equation: " + \
                str(a) + " x " + str(b)
            use_number.remove(get_use_number)
            temp.append(b)
        elif get_use_number % number == 0:
            a = get_use_number
            b = int(get_use_number/number)
            str_hint = "- this number satisfies the equationn: " + \
                str(a) + " / " + str(b)
            use_number.remove(get_use_number)
            temp.append(b)
        else:
            another_number = choice(
                [x for x in range(-(range_2), range_2) if x != number])
            if another_number > number:
                str_hint = "- number < " + str(another_number)
            else:
                str_hint = "- number >" + str(another_number)
    else:
        str_hint = get_primes(number)
    return use_number, str_hint, temp
