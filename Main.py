from Game import mainGame

def main():
    try:
        myGame = mainGame()
        myGame.start()
    except:
        print "Unable to start game"


if __name__ == "__main__":
    main();