from random import randint

print("rock paper scissors spock lizard!")
p1 = raw_input("what do you choose?")
p2int = randint(0, 4)
if p2int == 0:
    p2 = "rock"
elif p2int == 1:
    p2 = "paper"
elif p2int == 2:
    p2 = "scissors"
elif p2int == 3:
    p2 = "spock"
else:
    p2 = "lizard"
print("computer chooses " + p2)

if p1 == "rock":
    if p2 == "rock":
        print("it's a tie!")
    elif p2 == "paper":
        print("paper covers rock, pc wins!")
    elif p2 == "scissors":
        print("rock crushes scissors, you win!")
    elif p2 == "spock":
        print("spock vaporizes rock, pc wins!")
    elif p2 == "lizard":
        print("rock crushes lizard, you win!")
elif p1 == "paper":
    if p2 == "rock":
        print("paper covers rock, you win!")
    elif p2 == "paper":
        print("it's a tie!")
    elif p2 == "scissors":
        print("scissors cuts paper, pc wins!")
    elif p2 == "spock":
        print("paper disproves spock, you win!")
    elif p2 == "lizard":
        print("lizard eats paper, pc wins!")
elif p1 == "scissors":
    if p2 == "rock":
        print("rock crushes paper, pc wins!")
    elif p2 == "paper":
        print("scissors cuts paper, you win!")
    elif p2 == "scissors":
        print("it's a tie!")
    elif p2 == "spock":
        print("spock smashes scissors, pc wins!")
    elif p2 == "lizard":
        print("scissors decapitates lizard, you win!")
elif p1 == "spock":
    if p2 == "rock":
        print("spock vaporises rock, you win!")
    elif p2 == "paper":
        print("paper disproves spock, pc wins!")
    elif p2 == "scissors":
        print("spock smashes scissors, you win!")
    elif p2 == "spock":
        print("it's a tie!")
    elif p2 == "lizard":
        print("lizard poisons spock, pc wins!")
elif p1 == "lizard":
    if p2 == "rock":
        print("rock crushes lizard, pc wins!")
    elif p2 == "paper":
        print("lizard eats paper, you win!")
    elif p2 == "scissors":
        print("scissors decapitates lizard, pc wins!")
    elif p2 == "spock":
        print("lizard poisons spock, you win!")
    elif p2 == "lizard":
        print("it's a tie!")
else:
    print("no valid input, pc wins!")