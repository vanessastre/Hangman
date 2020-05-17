import getpass

def drawhangman(tries,movie):
    if (tries==0):
        print("___________\n|         |\n|\n|\n|\n|\n|__________")
    elif (tries==1):
        print("___________\n|         |\n|         O\n|\n|\n|\n|__________")
    elif (tries==2):
        print("___________\n|         |\n|         O\n|         |\n|         |\n|\n|__________")
    elif (tries==3):
        print("___________\n|         |\n|         O\n|        \|\n|         |\n|\n|__________")
    elif (tries==4):
        print("___________\n|         |\n|         O\n|        \|/\n|         |\n|\n|__________")
    elif (tries==5):
        print("___________\n|         |\n|         O\n|        \|/\n|         |\n|        /\n|__________")
    elif (tries==6):
        print("___________\n|         |\n|         O\n|        \|/\n|         |\n|        / \ \n|__________")
        print("\n You lose! \n")
        print("\n The movie was: ",movie)
        playAgain()
        return
def hideTheMovie(titleList,spaceList):
    for letter in titleList:
        if letter!=" ":
            spaceList.append("_")
        else:
            spaceList.append(" ")
    return

def wannaRisk(movie,tries):
    risk= input("\n Do you want to risk?  Yes/No ").upper()
    if risk=="YES":
        attempt=input("\n Write the movie title: ").upper()
        if attempt==movie:
            win()
        else:
            print("\nThat is not the movie.")
            tries=tries+1
            drawhangman(tries,movie)
    return

def win():
    print("\n You win!!!")
    playAgain()
    quit()

def playAgain():
    askPlayAgain=input("\n Do you want to play again? Yes/No \n").upper()
    if (askPlayAgain=="YES"):
        hangman()
    else:
        print("Thanks for playing Hangman with me")
    return

def hangman():
    tries=0
    movie= getpass.getpass("\n Type the movie title \n").upper()
    titleList= list(movie)
    spaceList=[]
    hideTheMovie(titleList,spaceList)
    newSpaceList= spaceList.copy()
    triesList= []
    print("Welcome to the Hangman.\nYou have to guess the movie title.\n")
    drawhangman(tries,movie)
    print (" ".join(spaceList))
    while tries<6:
        letter=input("\n Type a letter:  ").upper()
        if len(letter)>1:
            print("\n Only one letter!!!\n")
        elif letter=="":
            print("\n You have to type a letter\n")
        elif letter in triesList:
            print("\n You already said that letter \n")
            print("These are the letters you already said: ",triesList)
            print("\n")
        else:
            triesList.append(letter)
            i=0
            while i< len(movie):
                if letter==titleList[i]:
                    newSpaceList[i]=letter
                i= i+1
            if newSpaceList==spaceList:
                print("\n That letter is not here \n")
                tries= tries + 1
                drawhangman(tries,movie)
                if tries<6:
                    print("\n Try again \n")
                    print(" ".join(spaceList))
            elif titleList != spaceList:
                spaceList= newSpaceList[:]
                drawhangman(tries,movie)
                print(" ".join(spaceList))
                if titleList == spaceList:
                    win()
                else:
                    print ("\n Yeaaaaahhhh!\n")
                    wannaRisk(movie,tries)
hangman()