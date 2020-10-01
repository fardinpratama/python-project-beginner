# import my feature
from feature import (
    get_guess_numbers,
    clue_formula,
    zero_number,
    get_primes,
    get_range_number,
)

hearts = 3
# take the range of numbers you want to guess
get_range_number()


# Main Program
print("==================================")
print("======= Game Guess Number ========")
print("==================================")

while hearts:
    hints = []
    check_break = 0
    temp = []
    list_num_zero = [0, 1, 2, 3]
    numbers = get_guess_numbers()
    print("Hints:")
    number_guess = numbers['guess_number']
    use_numbers = numbers['list_use_number']
    while hearts:
        use_numbers, str_hint, temp = clue_formula(
            number_guess, use_numbers, temp, list_num_zero)
        hints.append(str_hint)
        for clue in hints:
            print(clue)
        print("Heart:", hearts)
        print("press 'q' for quit")
        your_guess = input("input your guess: ")
        if your_guess.lower() == 'q':
            check_break = 1
            break
        try:
            your_guess = int(your_guess)
        except:
            continue
        if number_guess == your_guess:
            print("* * * * * * * * * * * * * *  * * * ")
            print("*       You are Right!!!!        *")
            print("* * * * * * * * * * * * * *  * * * ")
            if hearts < 3:
                hearts += 1
            break
        else:
            print("* * * * * * * * * * * * * *  * * * ")
            print("*       You are wrong!!!!        *")
            print("* * * * * * * * * * * * * *  * * * ")
            hearts -= 1
            continue
    if check_break == 1:
        break
    print("="*40)
else:
    print("your heart has run out ")
    print("the answer is ", number_guess)
    print("Thank you for playing!!!!")
