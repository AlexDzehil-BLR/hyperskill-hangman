import random

map = ['python', 'java', 'kotlin', 'javascript']


def game():
    tryse = 0
    list_a = list(random.choice(map))
    list_b = ['-' for i in range(len(list_a))]
    set_set = set()
    print('H A N G M A N')
    while tryse < 8:
        print()
        if '-' not in list_b:
            break
        print(''.join(list_b))
        letter = input('Input a letter: ')
        if letter not in list_a:
            print("That letter doesn't appear in the word")
            tryse += 1
        if letter in set_set and letter in list_a:
            print('No improvements')
            tryse += 1
        if letter not in set_set and letter in list_a:
            set_set.add(letter)
        if letter in list_a:
            for i in range(len(list_a)):
                if list_a[i] == letter:
                    list_b[i] = letter


    if '-' not in list_b:
        print()
        print(''.join(list_b))
        print("""You guessed the word!
You survived!""")
    else:
        print('You lost!')
game()
