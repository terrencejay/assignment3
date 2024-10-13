place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place =="cave":
    print("You find a hidden treasure!")
    torch = input("would you like to light a torch or proceed in the dark? ")
    if torch == "proceed in the dark":
        print("You ran into a spiked wall beacuse you couldn't see.")
    else:
        print("You lit the torch in a gas chamber and blew up.")