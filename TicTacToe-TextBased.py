#!/usr/bin/env python3

board = [' ' for x in range(10)]
# board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def insertLetter(letter, pos):
	board[pos] = letter

def spaceIsFree(pos):
	return board[pos] == ' '
# This function will return a True and False value

def isWinner(bo,le):
	#given a board and a letter it will return true if that plaerhas won
	#using bo instead of board ans le instead of letter for simplicity

	return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)			  


def playerMove():
	run = True
	while run:			# keep running untill a valid move
		move = input('    Please select a postion to place an \'X\' (1-9):  ')
		try:			# making sure input is integer
			move = int(move)
			if move > 0 and move < 10:		# making ssure input is from 1-9
				if spaceIsFree(move):		# checking if move is valid
					run = False
					insertLetter('X', move)
				else:
					print('    This position is already occupied!')
			else:
				print('    Please type a number within range')
		except:
			print('    Please type a number!')

def selectRandom(li):
	import random
	ln =len(li)
	r = random.randrange(0,ln)
	return li[r]

def compMove():
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
		#create a list of possible moves
	move = 0 


	#Check for possible winning move to take or to block opponents winning move
	for let in ['O', 'X']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if isWinner(boardCopy, let):
				move = i
				return move


	# try to take one of the corners
	cornersOpen = []
	for i in possibleMoves:
		if i in [1,3,7,9]:
			cornersOpen.append(i)
	if len(cornersOpen) > 0:
		move = selectRandom(cornersOpen)
		return move


	# try to take the center
	if 5 in possibleMoves:
		move = 5
		return move

	#Take any edge
	edgesOpen = []
	for i in possibleMoves:
		if i in [2,4,6,8]:
			edgesOpen.append(i)

	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)

	return move



def isBoardFull(board):
	if board.count(' ') > 1: # Since we always have one element balnk the 0 pos
		return False
	else:
		return True

def printBoard(board):

# "board" is a list of 10 strings representing the board (ignore index 0)
	print('   |  |')
	print(' ' + board[1] + ' | ' + board[2] + '| ' + board[3])
	print('   |  |')
	print('------------')
	print('   |  |')
	print(' ' + board[4] + ' | ' + board[5] + '| ' + board[6])
	print('   |  |')
	print('------------')
	print('   |  |')
	print(' ' + board[7] + ' | ' + board[8] + '| ' + board[9])
	print('   |  |')


def main():
	#main game loop
	print("     Welcome to Tic Tac Toe to win complete a straight line of your letter (Diagonal , Horizaontal or Vertical). The board has postions 1-9 starting at the top left.  ")
	printBoard(board)

	while not(isBoardFull(board)):
		if not (isWinner(board, 'O')):
			playerMove()
			printBoard(board)
		else:
			print('    Computer Wins this time... ')
			break


		if not(isWinner(board, 'X')):
			move = compMove()
			if move == 0:
				print ('    Game is a Tie! No more spaces left to move.  ')
			else:
				insertLetter('O', move)
				print('    Computer place and \'o\' in the position', move, ':')
				printBoard(board)

		else:
			print('You win, Good Job!')
			break


	if isBoardFull(board):
		print('Game is a tie! No more Spaces left to move')


while True:
	answer = input('Do you want to play again? (Y/N)')
	if answer.lower() == 'y' or answer.lower == 'yes':
		board = [' ' for x in range(10)]
		print ('------------------------------')
		main()
	else:
		break

