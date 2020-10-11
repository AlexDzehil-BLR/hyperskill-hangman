import random

map = ['python', 'java', 'kotlin', 'javascript']


def game():
    tryse = 0
    a = random.choice(map)
    list_a = list(a)
    list_b = ['-' for i in range(len(a))]
    print('H A N G M A N')
    print()
    while tryse < 8:
        print(''.join(list_b))
        letter = input('Input a letter: ')
        if letter in a:
            for i in range(len(a)):
                if list_b[i].isalpha():
                    list_b[i] = list_a[i]
                elif list_a[i] == letter:
                    list_b[i] = letter
            print()
            tryse += 1
        else:
            print("That letter doesn't appear in the word")
            print()
            tryse += 1

    print()
    print("""Thanks for playing!
We'll see how well you did in the next stage""")

game()
