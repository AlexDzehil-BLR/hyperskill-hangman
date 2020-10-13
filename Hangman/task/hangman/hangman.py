import random

map = ['python', 'java', 'kotlin', 'javascript']


def game():
    tryse = 0
    alphabet = {
                'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o',
                'p', 'a', 's', 'd', 'f', 'g', 'h', 'j',
                'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
                }
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
        if len(letter) == 0 or len(letter) > 1:
            print('You should input a single letter')
        elif not bool(alphabet.intersection(set(letter))):
            print('Please enter a lowercase English letter')
        else:
            if letter not in list_a and letter not in set_set:
                print("That letter doesn't appear in the word")
                set_set.add(letter)
                tryse += 1
            elif letter in list_a and letter not in set_set:
                set_set.add(letter)
                for i in range(len(list_a)):
                    if list_a[i] == letter:
                        list_b[i] = letter
            elif letter in set_set:
                print("You've already guessed this letter")

    if '-' not in list_b:
        print()
        print(''.join(list_b))
        print("""You guessed the word!
You survived!""")
    else:
        print('You lost!')


game()
