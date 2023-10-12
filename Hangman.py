print ("Hello,Welcome to the HANGMAN")
print ("Start guessing...")

word = ("queue")

guesses = ''

turns = 10
while turns > 0:         

    failed = 0          

       

#comparing the chars here  
    for char in word:      

        if char in guesses:    
            print (char,end=""),    

        else:
            print ("_",end=""),     
            failed += 1    


    if failed == 0:        
        print (": You won")

        break            

    guess = input("Guess the word:") 

    guesses += guess                    



    if guess not in word:  
        turns -= 1        

        print ("Wrong")  
        print ( 'You have', + turns, 'attempts left !' )
        if turns == 0:           
            print ("You Lose"  )