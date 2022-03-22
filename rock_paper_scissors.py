import random

def game():
    print("Welcome to Rock Paper Scissors Game!!!")
    print('note : this game take random number')
    player = 0
    bot = 0
    
    while True:
        if bot == 10:
            print("bot is win this game!")
            break
        elif player == 10:
            print('player is win this game!')
            break
        
        print("-------------------------------")
        print("1-Rock | 2-Paper | 3-Scissors")
        
        guess = random.randint(1,3)
        
        while True:
            number = int(input("Inter : "))
            if number >= 4:
                print("please inter from 1 to 3 !!!")
            else:
                break    
                       
        if number == 1: # rock vs sissors
            if guess == 3:
                player += 1
                print("player is win!")    
        if number == 3: #sissors vs rock
            if guess == 1:
                bot +=1
                print("bot is win!")
        if number == 2: #paper vs rock
            if guess == 1:
                player +=1
                print('player is win!')
        if number == 1: #rock vs paper
            if guess == 2:
                bot +=1
                print('bot is win!')
        if number == 3:
            if guess == 2:
                player +=1
                print('player is win!')
        if number == 2:
            if guess == 3:
                bot += 1
                print('bot is win!')
        if number ==1:
            if guess == 1:
                print("draw!")
        if number ==2:
            if guess == 2:
                print("draw!")
        if number ==3:
            if guess == 3:
                print("draw!")

        print('bot take ',guess)       
        print('player : ',player)
        print('bot : ',bot) 
        
                        
game()
input('inter to exit :')
