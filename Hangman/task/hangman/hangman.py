# def hello():
#     return print("""H A N G M A N
# The game will be available soon.""")
#
# hello()

def game():
    a = 'python'
    print('H A N G M A N')
    b = input('Guess the word: ')
    if b == a:
        print('You survived!')
    else:
        print('You lost!')

game()