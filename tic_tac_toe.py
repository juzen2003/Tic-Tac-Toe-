# Tic Tac Toe game V1
# Dave Chang
# 2016/05/29

# pint out tic tac toe board
def displayBoardLocation():
	print '\nLocation'
	print ' 1 | 2 | 3 '
	print '-----------'
	print ' 4 | 5 | 6 '
	print '-----------'
	print ' 7 | 8 | 9 '
def displayBoard(info):	
	print '\nCurrent board'
	print ' %s | %s | %s ' %(info[0],info[1],info[2])
	print '-----------'
	print ' %s | %s | %s ' %(info[3],info[4],info[5])
	print '-----------'
	print ' %s | %s | %s ' %(info[6],info[7],info[8])

# ask for player's input
def takePlayerInput(board_info):
	valid_input = []
	for num in xrange(1,10):
		valid_input.append(str(num))
	user_input = raw_input('Please select a valid loaction: ')
	
	while user_input not in valid_input or board_info[int(user_input)-1] != ' ':
		user_input = raw_input('Please re-select a valid location: ')
	else:	
		return user_input

# define player's turn: Player 1: 'O', Player 2: 'X'
def playersTurn(turn):
	if turn % 2 != 0:
		print "\nPlayer 1's turn"
		return 'O'
	else:
		print "\nPlayer 2's turn"
		return 'X'
		
# place input on the board
def placeInput(user_marker, user_input, board_info):
	if user_marker == 'O':
		board_info[int(user_input)-1] = 'O'
	else: 
		board_info[int(user_input)-1] = 'X'
	displayBoardLocation()
	displayBoard(board_info)

# check current game result
def checkGame(board_info):
	if board_info[0] == board_info[1] == board_info[2] == 'O' or board_info[3] == board_info[4] == board_info[5] == 'O' or board_info[6] == board_info[7] == board_info[8] == 'O' or board_info[0] == board_info[3] == board_info[6] == 'O' or board_info[1] == board_info[4] == board_info[7] == 'O' or board_info[2] == board_info[5] == board_info[8] == 'O' or board_info[0] == board_info[4] == board_info[8] == 'O' or board_info[2] == board_info[4] == board_info[6] == 'O':
		print '\nPlayer 1 Win!'
		return True 
	elif board_info[0] == board_info[1] == board_info[2] == 'X' or board_info[3] == board_info[4] == board_info[5] == 'X' or board_info[6] == board_info[7] == board_info[8] == 'X' or board_info[0] == board_info[3] == board_info[6] == 'X' or board_info[1] == board_info[4] == board_info[7] == 'X' or board_info[2] == board_info[5] == board_info[8] == 'X' or board_info[0] == board_info[4] == board_info[8] == 'X' or board_info[2] == board_info[4] == board_info[6] == 'X':
		print '\nPlayer 2 Win!'
		return True
	elif board_info.count(' ') == 0:
		print "\nIt's a Tie!"
		return True
	else:
		print '\nContinue the game!'
		return False

# reset the game
def clear_board():
	board_info = [' ']*9
	current_turn = 1
	return (board_info, current_turn)

# define main function
def play_game():
	gameFinished = False
	# keep track of player markers & turns
	board_info = clear_board()[0]
	current_turn = clear_board()[1]
	
	displayBoardLocation()
	displayBoard(board_info)
	
	while gameFinished == False:
		user_marker = playersTurn(current_turn)
		user_input = takePlayerInput(board_info)
		placeInput(user_marker, user_input, board_info)
		current_turn += 1
		gameFinished = checkGame(board_info)
	else:
		print 'Game is Over!'
	
# main function
if __name__ == '__main__':
	
	play = True
	while play == True:
		play_game()
		play_again = raw_input('Play again? (Y/N) ')

		while play_again.lower() not in ['y', 'n']:
			play_again = raw_input('Play again? (Y/N) ')
		else:	
			if play_again.lower() == 'n':
				play = False
				print "I'm done with the game."
			else:
				play = True
