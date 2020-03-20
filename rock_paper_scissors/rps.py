#!/usr/bin/python

import sys

def rock_paper_scissors(n):
	results = []
	moves = ('rock', 'paper', 'scissors')

	def make_round(current_round, n):

		if n == 0:
			return results.append(current_round)
		
		for move in moves:
			make_round([*current_round, move], n-1)
		
	make_round([], n)

	return results

rock_paper_scissors(2)


if __name__ == "__main__":
	if len(sys.argv) > 1:
		num_plays = int(sys.argv[1])
		print(rock_paper_scissors(num_plays))
	else:
		print('Usage: rps.py [num_plays]')