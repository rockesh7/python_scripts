from random import randint

options = ['Stone', 'Paper', 'Scissor']

player = False

while player == False:
    computer = options[randint(0,2)]

    player = input('Stone, Paper, Scissor, Exit?   ')

    if player == 'Exit':
        player = True
    else:
        if player == computer:
            print('Tie!')

        elif player == 'Stone':
            if computer == 'Paper':
                print('You lose ' + computer + ' Covers ' + player)
            else:
                print('You Win ' + player + ' Breaks ' + computer)

        elif player == 'Paper':
            if computer == 'Scissor':
                print('You lose ' + computer + ' Cuts ' + player)
            else:
                print('You Win ' + player + ' Covers ' + computer)

        elif player == 'Scissor':
            if computer == 'Stone':
                print('You lose ' + computer + ' Breaks ' + player)
            else:
                print('You Win ' + player + ' Cuts ' + computer)
        else:
            print('Kindly pass the right play option')

        player = False