def dialogue():
    print("Hi! Am Kinaj!Nice to meet you!")
   
    name = input("What's your name dia:")
    if len(name) < 3:
        print("name too short", '\n')
        dialogue()
    if name.isdigit():
        print("This is't your name, cause you entered numbers. ")
        dialogue()
    Age_Bracket = int(input("How old are, ate be Honest?"))
    if Age_Bracket < 16:
        print("You are a minor, not allowd to use this program, <bye!")
        dialogue()

    Best_moments = input("Jazz me about your best Moments:")
    worst_moments = input("Jazz me about that one moment you almost gave up to the ghost:")
    if (worst_moments == 'none'):
        dialogue()
    Your_saviour = input("Who gave you another reason to live?")
    
    print(f"Sorry about that {name} but you it's part of life,How is life taking you?" )
    answer = input("good or bad: ")
    if (answer == "good"):
        print(f"Woooow! {name} Am happy for you dia.")
    if (answer == "Bad"):
            print(f"Sorry dia, {name} Just let Jesus take the wheel!")
    if (answer == "bad"):
        print(f"Sorry, {name} Just take lessons from all situations dia.!")   

    if (answer == "Good"):
        print(f"Awesome! {name} Whats the Secret Behind Good")    

    if (answer == "cool"):
        print(f"Hmmmmm! {name} May i ask why.....?")        


    if (answer == "awesome"):
        print(f"Beautiful! {name} Glory be to God.") 

    if (answer == "Fantastic"):
        print(f"Wonderfull! {name} Glory be to the almighty godd.")       

    if (answer == "50 50"):
        print(f"Sorry! {name} God will soon make Fantastic, in just a blink.")    
    else:
        print ('error')
    input("**Press the enter to continue**: ")
    print("So we meet again {name}!**Press enter to continue**")

    print(f"Ok ok. So you wanna continue with me, am really humbled.")
    dish= input("What is your favourite dish?")
    color = input(" wooow!! and what's your best color?")
    worst_dish = input("Whats your last to think of Meal?")
    worst_color=input("Ooooooh!! No, What's your worst color?")
    Best_scripture = input("What'ts your favourite Bible Verse?")
    any_advice = input("Whats your advice to the youths and teenagers.")

    input("**Press Enter to Continue**: ")
    print(f"It has been a pleasure chatting with you {name} and now it your turn, to ask me anything.")  
    you = input(':')
    print(f"Sorry{name} it's my show.")
    print("Thank you and goodbye!!")
    input("***Press CTRL + C to close the program***")     

dialogue()