from time import sleep

from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    if answer==question["answer"]:
        return True
    else:
        return False



def life(ques):


    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    print("Life line proccesing...........")
    sleep((2))

    a=ques["answer"]

    print(f'\tQuestion : {ques["name"]}')
    print(f'\t\tOptions:')
    if a==1:
        print(f'\t\t\tOption 1: {ques["option1"]}')
        print(f'\t\t\tOption 2: {ques["option2"]}')
    elif a==2:
        print(f'\t\t\tOption 1: {ques["option3"]}')
        print(f'\t\t\tOption 2: {ques["option2"]}')
    elif a==3:
        print(f'\t\t\tOption 1: {ques["option1"]}')
        print(f'\t\t\tOption 2: {ques["option3"]}')
    else:
        print(f'\t\t\tOption 1: {ques["option2"]}')
        print(f'\t\t\tOption 2: {ques["option4"]}')







def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("Welcome to Kaun Banega Coronapati")
    money=0
    lifeLine=1
    print("Press l for lifeline")



    for i in range(15):
        print(f'Money earned till now:Rs {money}')
        sleep(1)
      #print(money)
        if i+1==15:
            print("Congratulations!You have reached the final question. Now you wont be allowed to use any lifeline")
            lifeLine=lifeLine-1
            sleep(1)

        print(f"Life line left:{lifeLine}")
        sleep(1)


        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')

        ans = input('Your choice ( 1-4 ) : ')
        if ans=='quit':
            break

        elif ans=='l':
            if lifeLine==0:
                print("You have already used or this is the last question")
                sleep(1)
                print("Terminating...")
                sleep((1))
                break

            life(QUESTIONS[i] )
            ans = input('Your choice ( 1-2 ) : ')

            lifeLine=lifeLine-1


        if int(ans)<=0 or int(ans)>4:
            print("Wrong option chosen")
            sleep(1)
            print("Terminating.....")
            sleep((1))
            break


        if isAnswerCorrect(QUESTIONS[i], int(ans) ):


            print('\nAdbhutttttt !')
            money=QUESTIONS[i]["money"]

        else:


            print('\nApki khel idhar samapt hoti he...Subh ratri')

            if i<5:
                money=0

            elif i>=5 and i<11:
                money=10000

            else:
                money=320000

            break




        sleep(1)

        print("Agla sawal Apke Computer Screen ke upar yeh raha")

        sleep(1)

    if money==10000000:
        print("Ek Croreeeeeeeeeeeeeeee")
        print("Mubarak bad apko ")

    print(f'Money Earned:Rs {money}')
    print("Mutual funds me invest karna mat bhulna!!")

    # print the total money won in the end.


kbc()
