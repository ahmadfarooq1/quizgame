import os

# prints menu of options to choose from
def print_menu():
    
    print("="*35)
    print("|   Main  Menu - Select Options   |")
    print("="*35)
    print("| Please input the corresponding  | \n| option:                         |")
    print("|                                 |")
    print("|  (1) Start Quiz                 |") # input 1 to start quiz
    print("|  (2) Check Last High Score      |") # input 2 to check last high score
    print("|  (Q) Quit Game                  |") # input Q or q to quit
    print("="*35)

    return

# converts questions and answers from text files into lists for retrieval
def q_and_a_lists():

    a = [] # list to store answers without newline when reading from file
    q = [] # list to store questions without newline when reading from file

    answerFile = open("project #1/answers.txt", "r")
    questionFile = open("project #1/questions.txt", "r")
    qList = questionFile.readlines()
    aList = answerFile.readlines()

    if len(aList) != len(qList): # check if answers.txt and questions.txt have same amount of questions/answers
        if len(aList) > len(qList):
            print("Please check answers.txt because it has more lines than questions.txt")
        else:
            print("Please check questions.txt because it has more lines than answers.txt")
    else:
        for i in range(len(aList)): # append to a and q to remove newline
            a.append(aList[i].strip("\n"))
            q.append(qList[i].strip("\n"))

    return a, q

# starts quiz game
def start_quiz():

    tries = 3 # player only has 3 tries before game ends
    score = 0 # keeps track of current score
    index = 0 # index of question to ask and compare answer to

    ans, ques = q_and_a_lists() # calls q_and_a_lists function to create 2 lists with questions and answers in it

    # mini header to signal the start of game
    print("="*35)
    print("|          Starting Game          |")
    print("="*35)

    user_input = ask_question(index, ques)

    while (tries > 1): # keep running game until player runs out of tries

        if (user_input != ans[index]):
            tries -= 1
            print("Incorrect! You have {} tries left.\n".format(tries))
            user_input = ask_question(index, ques)
        else:
            score += 1
            print("Correct! Your current score is: {}\n".format(score))
            user_input = ask_question(index + 1, ques)
            index += 1

    if (tries - 1 == 0): # if tries = 0, prints message and exits game
        print("\nYou ran out of tries! You ended with a score of {}.".format(score))

    return score

# asks user the question depending on whether they got it right or not
# if user gets it right, i is increased by 1 but if not, asks the same question again
def ask_question(i, ques):

    print("Question:", ques[i])
    user_input = input("Answer: ")

    return user_input

# finds current highscore from scores text file instead of last score
def find_highscore():

    scores = [] # list to store scores without newline when reading from file

    scoreFile = open("project #1/scores.txt", "r")
    sList = scoreFile.readlines()

    for i in range(len(sList)): # append to scores to remove newline
        scores.append(sList[i].strip("\n"))

    scores.sort() # sort scores to find current highest score which is at the end of the list

    high_score = scores[-1]

    return high_score

# main function to run program
def main():

    print_menu() # prints menu

    while (True): # loop to ask for user input and run the game or quit

        user_input = input("\nOption: ")

        if (user_input == "1"):
            curr_score = start_quiz()

            with open("project #1/scores.txt", "a") as file: # stores score into scores text file
                file.write(str(curr_score) + "\n")

            break
        elif (user_input == "2"):
            if (os.path.exists("project #1/scores.txt") == False): # checks if score text file exists
                print("You have not played a game yet. Please play one before checking your highscore.")
            else:
                high_score = find_highscore()
                print("Your current high score is: {}".format(high_score))
        elif (user_input == "Q" or user_input == "q"):
            print("Exiting game.")
            break
        else:
            print("Invalid input. Please try again.")

    return

main()