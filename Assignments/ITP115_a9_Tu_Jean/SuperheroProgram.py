from ITP115_a9_Tu_Jean import Superhero


def main():
    play = True
    while play:
        # Gather information about superhero 1
        name1 = input("Enter fighter #1's name: ")
        type1 = input("Is fighter #1 a hero or a villain?: ")
        attack1 = input("Enter fighter#1's attack points: ")
        if attack1.isdigit():
            attack1 = int(attack1)
        else:
            while attack1.isdigit() == False:
                attack1 = input("Enter fighter#1's attack points: ")
                if attack1.isdigit():
                    attack1 = int(attack1)
                #else, just loop back to the top

        #Gather information about superhero 2
        name2 = input("\nEnter fighter #2's name: ")
        type2 = input("Is fighter #2 a hero or a villain?: ")
        attack2 = input("Enter fighter#2's attack points: ")
        if attack2.isdigit():
            attack2 = int(attack2)
        else:
            while attack2.isdigit() == False:
                print("INVALID INPUT, please enter a number")
                attack2 = input("Enter fighter#1's attack points: ")
                if attack2.isdigit():
                    attack2 = int(attack2)
                    # else, just loop back to the top

        s1 = Superhero(name1, type1, attack1)
        s2 = Superhero(name2, type2, attack2)
        print("\nFIGHTERS")
        print()
        print(s1.__str__())
        print(s2.__str__())
        print()

        print("\nBEGINNING BATTLE")

        #while neither of the players are dead
        roundNumber = 1
        while (s1.isDead() == False) and (s2.isDead() == False):
            s1.loseHealth(s2.getAttack())
            s2.loseHealth(s1.getAttack())
            print("============ Round "+ str(roundNumber) + " =============")
            print(s1.__str__())
            print(s2.__str__())
            print()
            roundNumber +=1
        if s1.isDead():
            print(s2.getName(), "won!")
        else:
            print(s1.getName(), "won!")
        cont = input("\nWould you like to play again? (y/n): ")
        print()
        if cont.lower() == "n":
            print("Goodbye!")
            play = False


main()