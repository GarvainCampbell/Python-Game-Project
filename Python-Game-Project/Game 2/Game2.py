# How do you play knock out with dice?
#To play Knock Out, every player rolls two dice.
#The dice are then added together. That sum is the score unless it was a 7.
#When a 7 is rolled the score of that player returns to 0.
def game2():

    print ("Knock Out!")
    print ("Rules-","Roll two dice","Add the dice to get your score","when a player gets 7, their score is reset to 0")
    (input("Press Enter to start"))
    import random
    min = 1
    max = 6
    score = 0
    roll_again = "yes"
   
    while roll_again == "yes" or roll_again == "Y" or roll_again == "y":
        print ("Rolling the dices...")
        print ("The values are....")
        a =(random.randint(min, max))
        b = (random.randint(min, max))
        print (a)
        print (b)
        
        if a + b == 7:
            score = 0
        else:
            score = a + b
        print("Your present score is ",score)
        
        

        roll_again = (input("Roll the dices again? "))
    if roll_again == "no" or roll_again == "N" or roll_again =="n":
        class Pov:
            def __init__(self, name, score):
                self.name = name
                self.score = score
        
        p1 = Pov(input("Enter Name "), score)
        print(p1.name)
        print("Your score is ", p1.score)
        # (remove # after merger)return main_menu
    elif roll_again != "Y" or "yes" or "y" or "n" or "N" or "no":
        return game2()

game2()
