'''provides random greetings'''
import random
sayings=('hello','welcome','hi','hey','aloha')

def greet():
	return random.choice(sayings)
