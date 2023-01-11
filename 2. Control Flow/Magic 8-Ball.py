# Magic 8-ball

# use the .randint() function from the random module to generate a random number from a range.
# generate a random number between 1 (inclusive) and 9 (inclusive).
import random
random_number = random.randint(1,9)

# 8-ball user dialogues
name = input("What is your name?")
print("Hello,", name, "!")
question = input("What do you wanna ask 8-ball?")
answer = ""

# mysterious inner workings of the *magic*
if random_number == 1:
  answer += "Yes - definitely."
elif random_number == 2:
  answer += "It is decidedly so."
elif random_number == 3:
  answer += "Without a doubt."
elif random_number == 4:
  answer += "Reply hazy, try again."
elif random_number == 5:
  answer += "Ask again later."
elif random_number == 6:
  answer += "Better not tell you now."
elif random_number == 7:
  answer += "My sources say no."
elif random_number == 8:
  answer += "Outlook not so good."
elif random_number == 9:
  answer += "Very doubtful."
else:
  answer += ("Error")

print(name,"asks:", question)
print("Magic 8-Ball's answer:",answer )
