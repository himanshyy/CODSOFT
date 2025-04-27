import random
item_list=["ROCK","PAPER","SCISSOR"]

user_choice=input("Enter your move= ROCK PAPER SCISSOR= ")
comp_choice= random.choice(item_list)

print(f"User choice={user_choice}, computer choice={comp_choice}")

if user_choice==comp_choice:
    print("both choice match: = Match Tie")

elif user_choice == "ROCK":
    if comp_choice == "PAPER":
        print("paper cover rocks: Computer wins")
    else:
        print("rock smashes scissor= you win") 

elif user_choice=="PAPER":
    if comp_choice=="SCISSOR":
        print("scissor cuts the paper, computer wins")
    else:
        print("paper covers rock, You win")

elif user_choice=="SCISSOR":
    if comp_choice=="PAPER":
        print("scissor cuts the paper, You win")
    else:
        print("rock smashes scissor, computer win")                       