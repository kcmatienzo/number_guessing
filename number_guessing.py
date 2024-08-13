import random
import math

#taking inputs
start = int(input("Enter start number:- "))
end = int(input("Enter end number:-  "))

# Generate random number between start and end numbers
x = random.randint(start, end)
print(x)
total_chances = math.ceil(math.log(end - start + 1, 2))
print(f"\nYou've only {total_chances} chances to guess the integer!\n")

# Initialize the number of guesses
count = 0
flag = False

# for calculation of monimum number of guesses depends upon range
while count < total_chances:
	count += 1

	#taking guessing number as input
	guess = int(input("Guess a number:- "))

	#Condition testing
	if x == guess:
		print("Congratulations, you did it in",count, "try!")
		#Once guesses, loop will break
		flag = True
		break
	elif x > guess:
		print("You guessed too small")
	elif x < guess:
		print("You guessed too high!")

#If guessing is more than allowed guesses, show this output
if not flag:
	print("\nThe number is %d" %x)
	print("\tBetter Luck Next Time!")