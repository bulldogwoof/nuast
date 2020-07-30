import random
player1score = 0
player2score = 0
turn = 1
times = 0
def diceroll():
    global turn
    global player1score
    global player2score
    finished = 0
    roundscore = 0
    while finished == 0:
        if turn == 1:
            go = input("Player 1, Type To roll...")
        if turn == 2:
            go = input("Player 2, Type To roll...")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("you rolled", dice1, "and", dice2)
        roundscore += (dice1 + dice2)
        if ((dice1 + dice2) % 2) == 0:
            roundscore += 10
        else:
            roundscore -= 5
        if dice1 == dice2:
            print("Doubles! Roll again")
            finished = 0
        else:
            finished = 1
    if turn == 1:
        player1score += roundscore
    if turn == 2:
        player2score += roundscore
    if turn == 1:
        turn = 2
    else:
        turn = 1
while times < 10:
    diceroll()
    print("player 1's score is", player1score)
    print("player 2's score is", player2score)
    times += 1
if player1score == player2score:
    while player1score == player2score:
        print("TieBreaker!")
        goo = input("Type to roll...")
        dice1 = random.randint(1, 6)
        player1score += dice1
        dice2 = random.randint(1, 6)
        player2score += dice2
        print("player 1 rolled", dice1)
        print("player 2 rolled", dice2)
if player1score > player2score:
    print("player 1 wins!")
    f = open('output.txt', 'w')
    f.write("Player 1 wins!" + '\n')
    f.write("player 1 score: " + '\n')
    f.write("player 2 score: " + '\n')
    f.close()
else:
    print("player 2 wins!")
    f = open('output.txt', 'w')
    f.write("Player 2 wins!" + '\n')
    f.write("player 2 score: " + '\n' )
    f.write( + "player 1 score: ", player2score)
    f.close()

e