
import random
from replit import clear
from game_data import data
from art import logo, vs

#Generate random data from data list
option_a = random.choice(data)
option_b = random.choice(data)

#keep track of user score
user_score = 0

game_on = True
while game_on:
	#display game logo
	print(logo) 
	print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
	# display versus logo 
	print(vs)
	print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")
# give user chance to choose from the random data
	user_choice = input("Who has more followers? Type 'A' or 'B':  ").lower()

#if user is right, compare the right answer to another data. Otherwise the user lose and game over
	if user_choice == 'a':
		if option_a["follower_count"] > option_b["follower_count"]:
			user_score += 1
			clear()
			print(f"You are right. Current score: {user_score}")
			option_a = option_b
			option_b = random.choice(data)
		else:
			print(f"Sorry, that's wrong. Final Score: {user_score}")
			game_on = False
	elif user_choice == 'b':
		if option_b["follower_count"] > option_a["follower_count"]:
			user_score += 1
			clear()
			print(f"You are right. Current score: {user_score}")
			option_a = option_b
			option_b = random.choice(data)
		else:
			print(f"Sorry, that's wrong. Final Score: {user_score}")
			game_on = False
	
	else:
		print("Invalid choice")
	