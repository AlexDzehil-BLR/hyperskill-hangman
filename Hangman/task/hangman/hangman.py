import random

map = ['python', 'java', 'kotlin', 'javascript']


def game_print():
    print('H A N G M A N')


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
    while tryse <= 8:
        print()
        if '-' not in list_b:
            print(''.join(list_b))
            print("""You guessed the word!
You survived!""")
            print()
            break
        print(''.join(list_b))
        letter = input('Input a letter: ')
        if len(letter) == 0 or len(letter) > 1:
            print('You should input a single letter')
        elif not bool(alphabet.intersection(set(letter))):
            print('It is not an ASCII lowercase letter')
        else:
            if letter not in list_a and letter not in set_set:
                tryse += 1
                if tryse == 8 and '-' in list_b:
                    print("""No such letter in the word
You lost!""")
                    print()
                    break
                print("No such letter in the word")
                set_set.add(letter)
            elif letter in list_a and letter not in set_set:
                set_set.add(letter)
                for i in range(len(list_a)):
                    if list_a[i] == letter:
                        list_b[i] = letter
            elif letter in set_set:
                print("You already typed this letter")


def play():
    while True:
        play_game = input('Type "play" to play the game, "exit" to quit: ')
        if play_game == 'exit':
            break
        elif play_game == 'play':
            game()


game_print()
play()
