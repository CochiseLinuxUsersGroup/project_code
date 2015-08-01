#paulbe practice code
#Rock Paper Scissors

import random;
import os;

print "Lets play rock, paper. scissors!"


#Setup the number of rounds.
#winp = input("How many points for a win? ") #broken set static var tround


#Set some variables
player_score = 0
computer_score = 0
tie = 0
rounds = 0
tround = 10 #change to increase or reduce rounds

#While loop
while rounds < tround:  #loops until round >= tround
	rounds = rounds + 1   #adds 1 to rounds each loop
	player = raw_input("Choose (R)ock (P)aper (S)cissors: ");  #user chooses r,p,s
	player = player.lower();
	while (player != 'r' and player != 'p' and player != 's'):  #verifies user choice will be understood
		print(player);
		player = input("Invalid Choice enter R, P, or S: ")
		player = player.lower();


	#handles computers choice
	os.system('clear');  #clear screen each round
	computer = random.randint(0,2);
	if (computer == 0):
		computer = "r";
	elif (computer == 1):
		computer = "p";
	elif (computer == 2):
		computer = "s";
	else:
		computer = "error";
	
	#Round handler
	if (player == computer):
		tie += 1;
		print("Draw");
	elif (player == 'r'):
		if (computer == 'p'):
			computer_score += 1;
			print("Computer Wins");
		else:
			player_score += 1;
			print("Player Wins");
	elif (player == 'p'):
		if (computer == 'r'):
			player_score += 1;
			print ("Player Wins");
		else:
			computer_score += 1;
			print ("Computer Wins");
	elif (player == 's'):
		if (computer == 'r'):
			computer_score += 1;
			print ("Computer Wins");
		else:
			player_score += 1;
			print ("Player Wins");
	print "Player: %r" % (player_score); #shows updated player_score
	print "Computer: %r" % (computer_score); #shows updated computer_score
	print "Draws: %r" % (tie); #shows update tie
	print "Round: %r of %r" % (rounds, tround); #show round of total rounds
else:
	if player_score == computer_score:  #ends in tie
		print "Player tied Computer"
	elif player_score > computer_score: #player wins
		print "Player WINS!  %r to %r" % (player_score, computer_score);
	elif player_score < computer_score: #player loses
		print "Computer WINS! %r to %r, Better luck next time." % (computer_score, player_score);
	else:
		print "Something weird happened.";

print "Thank you for playing!";

	
